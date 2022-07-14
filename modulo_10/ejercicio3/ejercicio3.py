import math

def costMin(lista):
  L = len(lista)
  matriz = [[0 for __ in range(0,L)] for _ in range(0,L)]

  for paso in range(1,L):
    for i in range(0, L-paso):
      j = i+paso
      minimo = lista[i][j]
      for k in range(i+1, j):
        minimo = min(minimo, matriz[k][j]+matriz[i][k])
      matriz[i][j] = minimo
  print(matriz[0][-1])


casos = int(input())
lista = []
for _ in range(0,casos):
  paradas = int(input())
  caso = []
  for i in range(0,paradas):
    filaActual = [x for x in input().split()]
    for j in range(0, paradas):
      if (i == j):
        filaActual[j] = 0
      elif (filaActual[j] == '*'):
        filaActual[j] = math.inf
      else:
        filaActual[j] = int(filaActual[j])
    caso.append(filaActual)
  lista.append(caso)

for i in lista:
  costMin(i)
