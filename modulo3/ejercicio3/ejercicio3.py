import itertools as it

casos = int(input())

for i in range(0,casos):
  ciudades = int(input())
  minimo = 1000000000
  auxiliar = 1000000000
  matriz = []
  for j in range(0,ciudades):
    linea = input().split()
    lineaAux = [-1 if i == "n.a" else int(i) for i in linea]
    matriz.append(lineaAux)
  

  for h in it.permutations(list(range(ciudades))):
    suma=0
    aux = True

    for m in range(len(h)-1):
      distancia = matriz[h[m]][h[m+1]]
      if distancia != -1:
        suma += distancia
      else:
        aux = False
        continue

    if aux :
      if suma < minimo:
        minimo = suma
  if minimo == auxiliar: 
    print('imposible')
  else: print(round(minimo/10))