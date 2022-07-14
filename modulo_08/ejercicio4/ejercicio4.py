import math

array = []

def parCercano(i, j, delta):
    global array
    medioX = array[int((i + j) / 2)][0]
    S = []
    for k in range(i, j + 1):
        punto = array[k]
        if(abs(punto[0] - medioX) < delta):
            S.append(punto)
    S.sort(key=lambda z: z[1])
    SY = S
    minD = delta
    for p in range(len(SY) - 1):
        q = p + 1
        while q < len(SY) and q <= p + 7:
            distancia = math.dist(SY[p], SY[q])
            if(distancia < minD):
                minD = distancia
            q += 1

    return minD


def parejas(i, j):
    if(i == j):
        return math.inf
    elif j - i == 1:
        return math.dist(array[i], array[j])
    else:
        medio = int((i + j) / 2)
        izquierda = parejas(i, medio)
        derecha = parejas(medio + 1, j)
        delta = min(izquierda, derecha)
        return parCercano(i, j, delta)


def distMin(arr):
    global array
    array = sorted(arr, key=lambda z: z[0])
    distancia = parejas(0, len(array) - 1)
    print(round(math.floor(distancia), 0))



casos = int(input())
finalArr = []
for _ in range(0, casos):
  robots = int(input())
  caseArr = []
  for __ in range(robots):
      caseArr.append([int(x) for x in input().split()])
  finalArr.append(caseArr)

for arr in finalArr:
  distMin(arr)
