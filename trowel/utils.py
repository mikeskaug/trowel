import math


def lon_to_tile(longitude, zoom):
    return math.floor((longitude + 180) / 360 * 2**zoom)

def lat_to_tile(lat, zoom):
    return math.floor((1 - math.log(math.tan(lat * math.pi / 180) + 1 / math.cos(lat * math.pi / 180)) / math.pi) / 2 * 2**zoom)

def tile_size(lon, lat, zoom):
    delta_lon = 360 / 2**zoom
    delta_lat = 170.1 / 2**zoom
    dimensions = degrees_to_meters(lon, lat, delta_lon, delta_lat)
    return dimensions

def degrees_to_meters(lon, lat, delLon, delLat):
    R = 6371000
    dLon = delLon * math.pi / 180
    a = math.cos(lat * math.pi / 180) * math.cos(lat * math.pi / 180) * math.sin(dLon / 2) * math.sin(dLon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    metersX = R * c

    dLat = delLat * math.pi / 180
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(lat * math.pi / 180) * math.cos(lat * math.pi / 180)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    metersY = R * c

    metersY = delLat * math.pi / 180 * R
    return {'x': metersX, 'y': metersY}

def lonlat_to_tile(lon, lat, zoom):
    return (lon_to_tile(lon, zoom), lat_to_tile(lat, zoom))

def tile_to_lonlat(X, Y, zoom):
    n = 2.0 ** zoom
    lon_deg = X / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * Y / n)))
    lat_deg = math.degrees(lat_rad)
    return (lon_deg, lat_deg)
