casos = int(input())

for _ in range(0,casos):
  casillas = int(input())
  lista = []
  for __ in range(0,casillas):
    lista.append(int(input()))
  
  if (len(lista) == 0):
    print(0)
  elif (len(lista) == 1):
    print(lista[0])
  elif (len(lista) == 2):
    print(max(lista))
  else:
    mejorCaso = [lista[0], max(lista[0], lista[1])]
    for i in range(2,casillas):
      numActual = lista[i]

      mejorAnterior = mejorCaso[i-1]

      mejor2Anterior = mejorCaso[i-2]

      sumaToma = numActual + mejor2Anterior

      sumaNoToma = mejorAnterior

      mejorCaso.append(max(sumaToma,sumaNoToma))

  print(mejorCaso[len(lista)-1])