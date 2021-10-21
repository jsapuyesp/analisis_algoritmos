import math

casos = int(input())

def cantidad(x):
  if x==2:return 2
  elif x==1:return 1
  rango = math.floor(math.sqrt(x))
  contador = 2
  for i in range(2,rango+1):
    if x%i == 0 and x//i != i:
      contador += 2
    elif x%i == 0 and x//i == i:
      contador += 1
  return contador


aux = [1]

for _ in range(0,casos):
  linea = input().split()
  x,y = int(linea[0]), int(linea[1])

  while y > aux[-1]:
    aux.append(aux[-1]+cantidad(aux[-1]))
  lista = list(filter(lambda a: a>=x and a<=y, aux))
  print(len(lista))
