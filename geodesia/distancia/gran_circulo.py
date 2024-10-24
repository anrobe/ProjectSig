import math

RADIO_TIERRA = 6371251.46

def calcular_distancia_gran_circulo(x1, y1, x2, y2):
    x_dist = math.radians(x1 - x2)
    y_dist = math.radians(y1 - y2)
    dist_sq = x_dist ** 2 + y_dist ** 2
    dist_rad = math.sqrt(dist_sq)
    return dist_rad * RADIO_TIERRA

if __name__ == "__main__":
    x1 = -90.212452861859035
    y1 = 32.316272202663704
    x2 = -88.952170968942525
    y2 = 30.438559624660321

    distancia = calcular_distancia_gran_circulo(x1, y1, x2, y2)
    print(distancia)
    # 251470.6807719638