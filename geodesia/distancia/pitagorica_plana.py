import math

def calcular_distancia_pitagorica(x1, y1, x2, y2):
    x_dist = x1 - x2
    y_dist = y1 - y2
    dist_sq = x_dist**2 + y_dist**2
    return math.sqrt(dist_sq)

if __name__ == "__main__":
    x1 = 456456.23
    y1 = 1279721.064
    x2 = 576628.34
    y2 = 1071740.33
    distancia = calcular_distancia_pitagorica(x1, y1, x2, y2)
    print(distancia)
    # 240202.668047278