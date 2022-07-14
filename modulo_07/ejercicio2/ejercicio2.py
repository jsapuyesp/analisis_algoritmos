def casaIdeal(lista):
  indice = 0
  lista = sorted(lista)
  largoLista = len(lista)
  medio = largoLista//2

  
  if (largoLista % 2 == 0):
    indice = medio - 1
  else:
    indice = medio
  casaSelecta = lista[indice]

  diferencia = 0

  for i in lista:
    if(i != casaSelecta):
      diferencia += abs(casaSelecta - i)
  
  print(str(casaSelecta)+' '+str(diferencia))



casas = int(input())
lista = []
for _ in range(0, casas):
  lista.append(int(input()))

casaIdeal(lista)