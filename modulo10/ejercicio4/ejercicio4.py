import math

def getNota(lista1, lista2):
  l1len = len(lista1) + 1
  l2len = len(lista2) + 1
  matriz = [[0 for __ in range(0,l2len)] for _ in range(0,l1len)]

  for i in range(1, l1len):
    prevL1 = i-1
    l1Element = lista1[prevL1]
    for j in range(1,l2len):
      prevL2 = j-1
      l2Element = lista2[prevL2]
      if (l1Element == l2Element):
        matriz[i][j] = matriz[prevL1][prevL2] + 1
      else:
        matriz[i][j] = max(matriz[prevL1][j], matriz[i][prevL2])
  
  return matriz[-1][-1]

def calP(puntosCorrectos, totalPuntos):
  return int(round(puntosCorrectos/totalPuntos * 100, 0))

casos = int(input())
lista = []
for _ in range(0,casos):
  largoCaso = int(input())
  seq = [x for x in input().split()]
  caso = [seq]

  for __ in range(0,largoCaso):
    caso.append([x for x in input().split()])
  lista.append(caso)

for i in range(0, casos):
  print(f"caso {i+1}:")
  lActual = lista[i]
  for j in range(1, len(lActual)):
    correctos = getNota(lActual[0], lActual[j])
    print(calP(correctos, len(lActual[0])))
  if(i != casos - 1):
    print("")