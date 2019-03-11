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

def tile_bounds(X, Y, zoom):
    '''
    Return the lat/lon bounds of a tile (min_lon, min_lat, max_lon, max_lat)
    '''
    min_lon, max_lat = tile_to_lonlat(X, Y, zoom)
    max_lon, min_lat = tile_to_lonlat(X+1, Y+1, zoom)

    return (min_lon, min_lat, max_lon, max_lat)

def bbox_to_tiles(min_lon, min_lat, max_lon, max_lat, zoom):
    '''
    Find the map tiles at the requested zoom level that cover a rectangular
    bounding box.

    Arguments:
    min_lon, min_lat, max_lon, max_lat - the minimum and maximum longitude and latitude
        extents of the bounding box
    zoom - The map tile zoom level for which to calculate the covering tiles

    Returns:
    A list of (zoom, X, Y) tuples for the map tiles
    '''
    lower_left_tile = lonlat_to_tile(min_lon, min_lat, zoom)
    upper_right_tile = lonlat_to_tile(max_lon, max_lat, zoom)

    tiles = []
    for X in range(lower_left_tile[0], upper_right_tile[0] + 1):
        for Y in range(upper_right_tile[1], lower_left_tile[1] + 1):
            tiles.append((zoom, X, Y))

    return tiles