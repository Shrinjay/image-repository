from geocoder import geocodefarm as geocode


def convert_to_dd(degrees, mins, seconds, ref):
    if ref == 'S' or ref == 'W':
        degrees = -degrees
        mins = -mins
        seconds = -seconds

    return degrees + float(mins) / 60 + float(seconds) / 3600


def get_latlong_from_exif(exif):
    gps = exif['GPSInfo']
    gps_lat = gps['GPSLatitude']
    gps_lon = gps['GPSLongitude']

    lat = convert_to_dd(gps_lat[0], gps_lat[1], gps_lat[2], gps['GPSLatitudeRef'])
    lon = convert_to_dd(gps_lon[0], gps_lon[1], gps_lon[2], gps['GPSLongitudeRef'])

    return lat, lon


def get_gps_json_from_exif(exif):
    return geocode([*get_latlong_from_exif(exif)], method='reverse').geojson
