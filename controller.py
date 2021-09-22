from flask import Blueprint, request, jsonify
from PIL import Image
from services.exif import get_exif
from services.geo import get_gps_json_from_exif
from services.model import CVModel
from database.db import DBSession, insert_image, query_images
from services.bucket import S3Manager
from config import BUCKET_NAME

controller = Blueprint('controller', __name__)
object_detector = CVModel()
session = DBSession().session()
s3 = S3Manager(BUCKET_NAME)


@controller.route('/images/', methods=['POST'])
def add_image():
    if 'new_image' in request.files:
        file_storage = request.files['new_image']
        file = file_storage.stream.read()
        img = Image.open(file_storage)
        exif = get_exif(file_storage)
        s3_key = request.form['title']
        city = None
        country = None
        objects = None

        if exif and 'GPSInfo' in exif:
            gps_json = get_gps_json_from_exif(exif)['features']
            if gps_json:
                location_info = gps_json[0]['properties']
                if 'city' in location_info:
                    city = location_info['city']
                if 'country' in location_info:
                    country = location_info['country']

        detected = object_detector.get_labels(img)

        if detected:
            objects = ','.join(detected)

        s3.put(s3_key, file)
        new_image = insert_image(session, s3_key, city, country, objects)

        return jsonify(new_image)


@controller.route('/images/', methods=['GET'])
def get_image():
    s3_key = request.args.get('title')
    city = request.args.get('city')
    country = request.args.get('country')
    object = request.args.get('object')

    images = query_images(session, s3_key, city, country, object)
    urls = list(map(lambda i: s3.get_url(i.s3_key), images))

    return jsonify(urls)
