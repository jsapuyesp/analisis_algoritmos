import bisect as bs

def parPerfecta(casos, lista, numero):
  indice = bs.bisect_left(lista, numero)
  if(indice == casos):
    cercano = lista[indice-1]
    print('la pareja mas cercana mide '+str(cercano))
  elif(lista[indice] == numero):
    print('hay por lo menos una pareja perfecta')
  elif(indice == 0):
    siguiente = lista[indice]
    print('la pareja mas cercana mide '+str(siguiente))
  else: 
    siguiente = lista[indice]
    diferenciaSig = abs(numero - siguiente)
    previoIndice = indice - 1
    previo = lista[previoIndice]
    diferenciaPrev = abs(numero - previo)
    if (diferenciaPrev < diferenciaSig):
      print('la pareja mas cercana mide '+str(previo))
    elif(diferenciaPrev > diferenciaSig):
      print('la pareja mas cercana mide '+str(siguiente))
    else:
      print('las parejas mas cercanas miden '+str(previo)+' y '+str(siguiente))

inputArr = [int(i) for i in input().split()]
numeros = inputArr[0]
parejaBuscar = inputArr[1]
lista = []
listaAux = []

for _ in range(0,numeros):
  lista.append(int(input()))

for _ in range(0,parejaBuscar):
  listaAux.append(int(input()))


lista = sorted(list(set(lista)))
numeros = len(lista)

for i in listaAux:
  parPerfecta(numeros, lista, i)
