

casos = int(input())

for _ in range(0,casos):
  tapas = int(input())
  lista_tapas = []
  for _ in range(0,tapas):
    tapa = int(input())
    lista_tapas.append(tapa)
  lista_tapas.sort(reverse=True)
  cantidad = 0
  while len(lista_tapas)>1:
    indexMax = 0
    indexMin = len(lista_tapas)-1
    while lista_tapas[indexMax] + lista_tapas[indexMin]< 1000:
      indexMin -= 1
      if indexMin < 1:
        break
    if indexMin < 1:
      break
    cantidad += 1
    lista_tapas = lista_tapas[indexMax + 1:indexMin]
  print(cantidad)

