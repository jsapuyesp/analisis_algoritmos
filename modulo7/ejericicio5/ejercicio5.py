def particion(lista, a, b, p):
  lista[a], lista[p] = lista[p], lista[a]
  i = a
  for j in range(a +1, b + 1):
    if lista[j] < lista[a]:
      i += 1
      lista[i],lista[j] = lista[j],lista[i]
    lista[i],lista[a] = lista[a],lista[i]
    return i

def quickSort(lista,a,b):
  if b-a > 0:
    global contador
    contador += 1
    p = a
    x = particion(lista, a, b, p)
    quickSort(lista,a,x-1)
    quickSort(lista, x+1,b)


entrada = int(input())
for _ in range(0,entrada):
  lista = [int(x) for x in input().split()]
  contador = 0
  quickSort(lista, 0, len(lista)-1)
  print(contador)
