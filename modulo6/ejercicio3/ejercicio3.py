

def par(largo,lista, pareja):
  lista = sorted(lista)
  menorPareja, pendiente = divmod(pareja, largo)
  menorPareja = menorPareja -1 if(pendiente == 0) else menorPareja
  pendiente -= 1
  base = lista[menorPareja]
  segundaPareja = lista[pendiente]
  print(str(base)+' '+str(segundaPareja))



inputArr = [int(i) for i in input().split()]
numeros = inputArr[0]
parejaBuscar = inputArr[1]
lista = []

for _ in range(0,numeros):
  lista.append(int(input()))


par(numeros,lista,parejaBuscar)