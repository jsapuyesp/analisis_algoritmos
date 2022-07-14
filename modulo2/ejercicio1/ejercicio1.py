import math

casos= int(input())

for i in range (0,casos):
  linea = input().split()
  map_linea = map(int, linea)
  lista_int = list(map_linea)
  lcm = lista_int[0]
  for i in range (1,len(lista_int)) :
    lcm = math.lcm(lcm,lista_int[i])
  print(lcm)
