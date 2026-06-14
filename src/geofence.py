SAFE_LAT = 17.000000
SAFE_LON = 82.000000

def check_geofence(lat, lon):

    if abs(lat - SAFE_LAT) <= 0.02 and abs(lon - SAFE_LON) <= 0.02:
        return "SAFE"

    return "OUTSIDE"