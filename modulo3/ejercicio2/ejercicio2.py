import itertools as it

casos = int(input())

for i in range(0,casos):
  
  linea = input().split()
  n = int(linea[0])
  linea.pop(0)
  map_linea = map(int, linea)
  lista_int = list(map_linea)
  
  p = list(it.product([0,1], repeat = len(lista_int)))
  
  tiempoMax = 0

  for c in p:
    tiempoAux = sum([x*y for x,y in zip(c,lista_int)])

    if n >= tiempoAux:
      if tiempoAux > tiempoMax:
        tiempoMax = tiempoAux


  print(n-tiempoMax)

