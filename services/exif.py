from PIL import Image, ExifTags


def _clean_exif_key(raw_key):
    if raw_key in ExifTags.TAGS:
        return ExifTags.TAGS[raw_key]
    else:
        return None


def _clean_exif_geo_key(raw_key):
    if raw_key in ExifTags.GPSTAGS:
        return ExifTags.GPSTAGS[raw_key]
    else:
        return None


def _clean_exif_geo(raw_geo):
    return {_clean_exif_geo_key(k): v for k, v in raw_geo.items()}


def _clean_exif(raw_exif):
    exif = {_clean_exif_key(k): v for k, v in raw_exif.items()}
    if 'GPSInfo' in exif:
        exif['GPSInfo'] = _clean_exif_geo(exif['GPSInfo'])
    return exif


def get_exif(img):
    raw_exif = Image.open(img)._getexif()
    if raw_exif:
        return _clean_exif(raw_exif)
    else:
        return None
