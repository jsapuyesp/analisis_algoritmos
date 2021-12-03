import math

array = []

def minDistancia(x,y,delta):
  global array
  indexMedio = int((x+y)/2)
  puntoXmedio = array[indexMedio][0]
  S = []
  for k in range(x,y+1):
    punto = array[k]
    if(abs(punto[0]-puntoXmedio)<delta):
      S.append(punto)
  Sy = sorted(S, key= lambda z: z[1])
  syLength = len(Sy)
  distMin = delta

  for p in range(0, syLength - 1):
    q = p+1
    while (q < syLength) and (q <= p+7):
      p1 = Sy[p]
      p2 = Sy[q]
      if(p1[2] != p2[2]):
        distanciaActual = math.dist(p1[:2], p2[:2])
        if(distanciaActual < distMin):
          distMin = distanciaActual
      q += 1
  return distMin

def getDist(x,y):
  global array
  if(x==y):
    return math.inf
  elif(y-x == 1):
    p1 = array[x]
    p2 = array[y]
    if(p1[2] != p2[2]):
      return math.dist(p1[:2], p2[:2])
    else:
      return math.inf
  else:
    indexMedio = int((x+y)/2)
    minIzquierda = getDist(x,indexMedio)
    minDerecha = getDist(indexMedio+1, y)
    delta = min(minIzquierda, minDerecha)
    return minDistancia(x,y,delta)


def getMinRival(x):
  global array
  array = sorted(x, key=lambda z:z[0])
  distResult = getDist(0, len(array)-1)
  if(math.isinf(distResult)):
    print('INF')
  else: print(round(distResult,1))


arrayFinal = []
while(True):
  planetas = int(input())
  if(planetas == 0):
    break
  arrCaso = []
  for _ in range(0,planetas):
    inputArr = input().split()
    inputArr[0] = int(inputArr[0])
    inputArr[1] = int(inputArr[1])
    arrCaso.append(inputArr)
  arrayFinal.append(arrCaso)

for case in arrayFinal:
  getMinRival(case)