import math

def isViaje(lista):
  grafo = lista[0]
  relaciones = lista[1]

  grafo['0']['spd'] = 0

  for _ in range(1, len(relaciones)):
    for relacion in relaciones:
      oNodo = grafo[relacion[0]]
      dNodo = grafo[relacion[1]]
      costo = relacion[2]
      actSum = oNodo['spd'] + costo
      if (actSum < dNodo['spd']):
        dNodo['spd'] = actSum
  
  posible = False

  for relacion in relaciones:
    oNodo = grafo[relacion[0]]
    dNodo = grafo[relacion[1]]
    costo = relacion[2]
    actSum = oNodo['spd'] + costo
    if (actSum < dNodo['spd']):
      posible = True
      break
  
  if(posible):
    print('es posible viajar al big bang')
  else:
    print('no es posible')

def main():
  casos = int(input())
  arr = []

  for _ in range(casos):
    inputArr = input().split()
    sSolar = int(inputArr[0])
    agujeros = int(inputArr[1])

    iGrafo = {}

    for i in range(sSolar):
      iGrafo[str(i)] = {
        'spd': math.inf
      }
    
    lRelaciones = []
    for __ in range(agujeros):
      lRelacion = input().split()
      lRelacion[2] = int(lRelacion[2])
      lRelaciones.append(lRelacion)
    
    arr.append([iGrafo, lRelaciones])
  
  for i in arr:
    isViaje(i)


main()
