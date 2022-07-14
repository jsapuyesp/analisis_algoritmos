import math


def cabo(lista: list):
  lenLista = len(lista)

  M = [[0 for __ in range(0,lenLista)] for _ in range(0,lenLista)]

  for i in range(0,lenLista):
    M[i][i] = lista[i]
  
  for nodo in range(1, lenLista):
    for i in range(0, lenLista-nodo):
      j = i + nodo
      bajo = math.inf
      for r in range(i, j + 1):
        r1 = r - 1
        r2 = r + 1
        item1 = 0 if r1 < 0 else M[i][r1]
        item2 = 0 if r2 >= lenLista else M[r2][j]
        bajo = min(bajo, item1+item2+sum(lista[i:j+1]))
      M[i][j] = bajo
  
  print(M[0][-1])

def main():
  casos = int(input())
  lista= []

  for _ in range(casos):
    lista.append([int(x) for x in input().split()])
  
  for item in lista:
    cabo(item)

main()