import math

def minimoBilletes(lista : list):
  columnas = lista[0] + 1
  arrBilletes = lista[1:]
  largoBilletes = len(arrBilletes) + 1

  matriz = [[math.inf for __ in range(0, columnas)] for _ in range(0, largoBilletes)]

  for i in range(0, largoBilletes):
    matriz[i][0] = 0
  
  for i in range(1, largoBilletes):
    prev = i-1
    billetesActual = arrBilletes[prev]
    for j in range(1, columnas):
      itemPrev = matriz[prev][j]
      if billetesActual <= j:
        k = j - billetesActual
        matriz[i][j] = min(1 + matriz[i][k], itemPrev)
      else:
        matriz[i][j] = prev
  print(matriz[-1][-1])

casos = int(input())
arr=[]

for _ in range(0, casos):
  lista = [int(x) for x in input().split()]
  arr.append(lista)

for __ in arr:
  minimoBilletes(__)

