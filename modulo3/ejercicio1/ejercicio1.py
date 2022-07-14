from itertools import permutations


casos = int(input())


for i in range(0,casos):
  contador = 0
  linea = input().split()
  n = int(linea[0])
  linea.pop(0)
  map_linea = map(int, linea)
  lista_int = list(map_linea) #Tengo la lista de enteros
  permutaciones = permutations(lista_int)
  for p in permutaciones:
    l1 = sum(p[0:4])
    l2 = sum(p[3:7])
    l3 = sum(p[6:]+p[0:1])
    if l1 == l2 and l2 == l3 and l3 == n:
      contador += 1
  print(contador)  
