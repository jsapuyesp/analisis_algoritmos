import heapq
import math

auxMatrix = []
distMatrix = []
filas = 0
columnas = 0

def getRelaciones(i,j):
  global distMatrix
  global filas
  global columnas

  prevFila = i - 1
  nextFila = i + 1
  prevCol = j - 1
  nextCol = j + 1

  relaciones = []

  if (prevFila >= 0):
    relaciones.append([distMatrix[prevFila][j], [prevFila, j]])
  if (prevCol >= 0):
    relaciones.append([distMatrix[i][prevCol], [i, prevCol]])
  if (nextFila < filas):
    relaciones.append([distMatrix[nextFila][j], [nextFila, j]])
  if (nextCol < columnas):
    relaciones.append([distMatrix[i][nextCol], [i, nextCol]])
  
  return relaciones

def minCosto(mat: list):
  global auxMatrix
  global distMatrix
  global filas
  global columnas

  auxMatrix = mat
  filas = len(auxMatrix)
  columnas = len(auxMatrix[0])

  distMatrix = [[math.inf for _ in range(columnas)] for __ in range(filas)]

  distMatrix[0][0] = 0

  pq = []
  heapq.heapify(pq)

  nodo = [0, [0,0]]
  heapq.heappush(pq, nodo)

  while len(pq) > 0:
    u = heapq.heappop(pq)
    relaciones = getRelaciones(u[1][0], u[1][1])

    for nNodo in relaciones:
      nexSum = u[0] + auxMatrix[nNodo[1][0]][nNodo[1][1]]
      if (nexSum < nNodo[0]):
        nNodo[0] = nexSum

        distMatrix[nNodo[1][0]][nNodo[1][1]] = nexSum
        heapq.heappush(pq, nNodo)
  print(distMatrix[-1][-1])

def main():
  casos = int(input())
  lista = []
  for _ in range(0, casos):
    inputLista = input().split()
    filasNum = int(inputLista[0])
    mat = []
    for __ in range(0,filasNum):
      mat.append([int(x) for x in input().split()])
    lista.append(mat)
  
  for mat in lista:
    minCosto(mat)


main()