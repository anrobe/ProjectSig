import math

# Parameters of the Ellipsoid (according to IGN-Peru documentation)
SEMI_MAJOR_AXIS = 6378137  # semi-major axis (meters)
FLATTENING = 1 / 298.257222101  # flattening
SEMI_MINOR_AXIS = SEMI_MAJOR_AXIS * (1 - FLATTENING)  # semi-minor axis (meters)


def vincenty_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the Vincenty distance between two points on the Earth's surface.

    Parameters:
    lat1, lon1: Latitude and Longitude of point 1 (degrees)
    lat2, lon2: Latitude and Longitude of point 2 (degrees)

    Returns:
    distance: Distance between the two points (meters)
    """
    L = math.radians(lon2 - lon1)
    U1 = math.atan((1 - FLATTENING) * math.tan(math.radians(lat1)))
    U2 = math.atan((1 - FLATTENING) * math.tan(math.radians(lat2)))
    sinU1, cosU1 = math.sin(U1), math.cos(U1)
    sinU2, cosU2 = math.sin(U2), math.cos(U2)

    lam = L
    for _ in range(100):
        sinLam, cosLam = math.sin(lam), math.cos(lam)
        sinSigma = math.sqrt((cosU2 * sinLam) ** 2 + (cosU1 * sinU2 - sinU1 * cosU2 * cosLam) ** 2)
        if sinSigma == 0:
            return 0  # coincident points
        cosSigma = sinU1 * sinU2 + cosU1 * cosU2 * cosLam
        sigma = math.atan2(sinSigma, cosSigma)
        sinAlpha = cosU1 * cosU2 * sinLam / sinSigma
        cosSqAlpha = 1 - sinAlpha ** 2
        cos2SigmaM = cosSigma - 2 * sinU1 * sinU2 / cosSqAlpha
        if math.isnan(cos2SigmaM):
            cos2SigmaM = 0  # equatorial line
        C = FLATTENING / 16 * cosSqAlpha * (4 + FLATTENING * (4 - 3 * cosSqAlpha))
        lamPrev = lam
        lam = L + (1 - C) * FLATTENING * sinAlpha * (
                    sigma + C * sinSigma * (cos2SigmaM + C * cosSigma * (-1 + 2 * cos2SigmaM ** 2)))
        if abs(lam - lamPrev) < 1e-12:
            break

    uSq = cosSqAlpha * (SEMI_MAJOR_AXIS ** 2 - SEMI_MINOR_AXIS ** 2) / (SEMI_MINOR_AXIS ** 2)
    A = 1 + uSq / 16384 * (4096 + uSq * (-768 + uSq * (320 - 175 * uSq)))
    B = uSq / 1024 * (256 + uSq * (-128 + uSq * (74 - 47 * uSq)))
    deltaSigma = B * sinSigma * (cos2SigmaM + B / 4 * (
                cosSigma * (-1 + 2 * cos2SigmaM ** 2) - B / 6 * cos2SigmaM * (-3 + 4 * sinSigma ** 2) * (
                    -3 + 4 * cos2SigmaM ** 2)))
    distance = SEMI_MINOR_AXIS * A * (sigma - deltaSigma)

    return distance


if __name__ == "__main__":
    # Coordinates of the points (latitude and longitude in degrees)
    lat1, lon1 = 32.316272202663704, -90.212452861859035
    lat2, lon2 = 30.438559624660321, -88.952170968942525

    distance = vincenty_distance(lat1, lon1, lat2, lon2)
    print(f"Vincenty distance: {distance:.2f} meters")