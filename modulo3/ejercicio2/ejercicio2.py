

casos = int(input())

for i in range(0,casos):
  contador = 0
  linea = input().split()
  n = int(linea[0])
  linea.pop(0)
  map_linea = map(int, linea)
  lista_int = list(map_linea)