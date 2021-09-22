from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from orm.Image import Base, Image


class DBSession:
    def __init__(self):
        engine = create_engine('sqlite:///photos.db?check_same_thread=False')
        self.session = sessionmaker(bind=engine)
        Base.metadata.create_all(engine, checkfirst=True)


def insert_image(session, s3_key, city, country, objects):
    new_image = Image(s3_key=s3_key, city=city, country=country, objects=objects)
    session.add(new_image)
    session.commit()
    return new_image.id


def query_images(session, s3_key, city, country, object):
    images = session.query(Image)

    if s3_key:
        images = images.filter(Image.s3_key == s3_key)

    if city:
        images = images.filter(Image.city == city)

    if country:
        images = images.filter(Image.country == country)

    if object:
        images = images.filter(Image.objects.contains(object))

    return images
