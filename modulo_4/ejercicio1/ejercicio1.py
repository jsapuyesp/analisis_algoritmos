import itertools as it

casos = int(input())

for i in range(0,casos):
  linea = input().split()
  map_linea = map(int, linea)
  lista_int = list(map_linea)
  n = lista_int[0]
  opciones = [-1] * n
  opciones[lista_int[1] - 1] = lista_int[2] - 1
  opciones[lista_int[3] - 1] = lista_int[4] - 1
  listFaltantes = []
  for i in range(n):
    if i != lista_int[2] - 1 and i != lista_int[4] - 1:
      listFaltantes.append(i)
  p = list(it.permutations(listFaltantes))
  opcion = []
  for j in p:
    pAux = list(opciones)
    c = 0
    good = True
    for k in range(n):
      if opciones[k] == -1:
        pAux[k] = j[c]
        c += 1
    if len(set(pAux)) == n:
      opcion.append(pAux)
  contador = 0
  for j in opcion:
    funciona = True
    for k in range(1, n):
      for l in range(k):
        if abs(k - l) == abs(j[k] - j[l]):
          funciona = False
          break
        if not funciona:
          break
    if funciona:
      contador += 1
  print(contador)