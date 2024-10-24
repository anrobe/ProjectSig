import math

RADIO_TIERRA = 6371251.46

def calcular_distancia_haversine(x1, y1, x2, y2):
    x_dist = math.radians(x1 - x2)
    y_dist = math.radians(y1 - y2)
    y1_rad = math.radians(y1)
    y2_rad = math.radians(y2)

    a = math.sin(y_dist / 2) ** 2 + math.sin(x_dist / 2) ** 2 * math.cos(y1_rad) * math.cos(y2_rad)
    c = 2 * math.asin(math.sqrt(a))
    return c * RADIO_TIERRA

if __name__ == "__main__":
    x1 = -90.212452861859035
    y1 = 32.316272202663704
    x2 = -88.952170968942525
    y2 = 30.438559624660321

    distancia = calcular_distancia_haversine(x1, y1, x2, y2)

    print(f"Distancia: {distancia / 1000:.2f} km")  # Distancia en km
    print(f"Distancia: {distancia:.2f} m")  # Distancia en m