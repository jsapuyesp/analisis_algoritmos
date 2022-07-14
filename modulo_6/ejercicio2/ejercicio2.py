
def buscar(lista,numero):
  lista.sort()
  try:
    indice = lista.index(numero)
    print(str(numero)+' se encuentra en '+str(indice+1))
  except:
    print(str(numero)+' no se encuentra')

inputArr = [int(i) for i in input().split()]
numerosLen = inputArr[0]
busquedaLen = inputArr[1]
numeros = []
busquedas = []

for _ in range(0,numerosLen):
  numeros.append(int(input()))
for _ in range(0,busquedaLen):
  busquedas.append(int(input()))

for i in busquedas:
  buscar(numeros, i)
