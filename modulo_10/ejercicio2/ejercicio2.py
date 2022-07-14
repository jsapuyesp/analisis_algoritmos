def getCity(lista):
  x1 = lista[0]
  x2 = lista[1]
  x1Length = len(x1)+1
  x2Length = len(x2)+1

  matriz = [[0 for __ in range(0,x2Length)] for _ in range(0,x1Length)]

  for i in range(1, x1Length):
    prevX1Index = i-1
    actX1Element = x1[prevX1Index]
    for j in range(1, x2Length):
      prevX2Index = j-1
      actX2Element = x2[prevX2Index]
      if (actX1Element == actX2Element):
        matriz[i][j] = matriz[prevX1Index][prevX2Index] + 1
      else:
        matriz[i][j] = max(matriz[prevX1Index][j], matriz[i][prevX2Index])
  
  print(matriz[-1][-1])

casos = int(input())
lista = []
for _ in range(0,casos):
  lista.append([x for x in input().split()])
for caso in lista:
  getCity(caso)