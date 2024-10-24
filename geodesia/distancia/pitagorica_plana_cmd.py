import math


def calcular_distancia_pitagorica(x1, y1, x2, y2):
    x_dist = x1 - x2
    y_dist = y1 - y2
    dist_sq = x_dist ** 2 + y_dist ** 2
    return math.sqrt(dist_sq)


if __name__ == "__main__":
    x1 = float(input("Ingrese la coordenada x1: "))
    y1 = float(input("Ingrese la coordenada y1: "))
    x2 = float(input("Ingrese la coordenada x2: "))
    y2 = float(input("Ingrese la coordenada y2: "))

    distancia = calcular_distancia_pitagorica(x1, y1, x2, y2)
    print(f"La distancia pitagórica es: {distancia}")