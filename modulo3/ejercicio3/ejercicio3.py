import itertools as it

casos = int(input())

for i in range(0,casos):
  ciudades = int(input())
  matriz = []
  for j in range(0,ciudades):
    linea = input().split()
    matriz.append(linea)
  print(matriz)