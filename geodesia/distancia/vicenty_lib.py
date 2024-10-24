from geopy.distance import geodesic

def calcular_distancia_geodesica(lat1, lon1, lat2, lon2):
    """
    Calculate the geodesic distance between two points using the WGS-84 ellipsoid.

    Parameters:
    lat1, lon1: Latitude and Longitude of point 1 (degrees)
    lat2, lon2: Latitude and Longitude of point 2 (degrees)

    Returns:
    distance: Distance between the two points (meters)

                  model             major (km)   minor (km)     flattening
    ELLIPSOIDS = {'WGS-84':        (6378.137,    6356.7523142,  1 / 298.257223563),
                  'GRS-80':        (6378.137,    6356.7523141,  1 / 298.257222101),
                  'Airy (1830)':   (6377.563396, 6356.256909,   1 / 299.3249646),
                  'Intl 1924':     (6378.388,    6356.911946,   1 / 297.0),
                  'Clarke (1880)': (6378.249145, 6356.51486955, 1 / 293.465),
                  'GRS-67':        (6378.1600,   6356.774719,   1 / 298.25),
                  }
    """
    point_a = (lat1, lon1)
    point_b = (lat2, lon2)
    return geodesic(point_a, point_b, ellipsoid='WGS-84').meters

if __name__ == "__main__":
    # Coordinates of the points (latitude and longitude in degrees)
    lat1, lon1 = 32.316272202663704, -90.212452861859035
    lat2, lon2 = 30.438559624660321, -88.952170968942525

    distancia = calcular_distancia_geodesica(lat1, lon1, lat2, lon2)
    print(f"La distancia geodésica en metros es: {distancia:.2f}")