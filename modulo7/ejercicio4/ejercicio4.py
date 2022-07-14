def diferencia(lista, indice):
  indice -= 1
  antipodeI = len(lista) - 1 - indice
  lista = sorted(lista)
  elemento = lista[indice]
  antipodeE = lista[antipodeI]
  print(abs(elemento-antipodeE))

entrada = input().split()
elementos = int(entrada[0])
indice = int(entrada[1])

listaAux = []

for _ in range(0, elementos):
  listaAux.append(int(input()))

diferencia(listaAux, indice)
