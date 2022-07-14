import math


def maxScore(lista):
  lenLista = len(lista)
  lista.sort()

  M = [[lista[i] for j in range(0,lenLista)] for  i in range(0, lenLista)]

  for matriz in range(1, lenLista):
    for i in range(0, lenLista-matriz):
      j = i + matriz
      maxItem = [0, 0]
      for k in range(i,j):
        item1 = M[i][k]
        item2 = M[k+1][j]
        S = item1[1] + item2[1]
        S += divisores(S)

        if(S >= maxItem[1]):
          maxItem = [max(item1[0], item2[0]), S]

      M[i][j] = maxItem

  print(M[0][-1][1])

def divisores(n):
  contador = 0
  for i in range(1, int((math.sqrt(n))+1)):
    if n%i==0:
      contador = contador + 1 if n/i == i else contador +2
  return contador

def main():
  cases = int(input())
  lista = []
  for _ in range(0, cases):
    numeroCartas = int(input())
    listaCartas = []
    for __ in range(0, numeroCartas):
      listaCartas.append([int(x) for x in input().split()])
    
    lista.append(listaCartas)
  
  for item in lista:
    maxScore(item)



main()