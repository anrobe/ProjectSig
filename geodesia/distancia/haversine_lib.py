from geopy.distance import great_circle

def calcular_distancia_gran_circulo(x1, y1, x2, y2):
    point_a = (y1, x1)
    point_b = (y2, x2)
    return great_circle(point_a, point_b).meters

if __name__ == "__main__":
    x1 = -90.212452861859035
    y1 = 32.316272202663704
    x2 = -88.952170968942525
    y2 = 30.438559624660321

    distancia = calcular_distancia_gran_circulo(x1, y1, x2, y2)

    print(f"La distancia del Gran Círculo en metros es: {distancia:.2f}")