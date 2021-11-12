
casos = int(input())

for _ in range(0,casos):
  linea = input().split()
  map_linea = map(int, linea)
  lista_int = list(map_linea)
  lista_int.sort(reverse=True)

  lista_triadas = [lista_int[j:j+3] for j in range(0,len(lista_int), 3)]

  descuentoMax = 0

  for i in lista_triadas:
    if len(i) == 3:
      descuentoMax += i[2]
  print(descuentoMax)
