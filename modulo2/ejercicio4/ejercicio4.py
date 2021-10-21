casos = int(input())

def calcular(z,y):
  a = z if z >= y else y
  b = y if z >= y else z
  while b != 0: 
    a, b = b, a%b
  return a


for q in range(0,casos):
  linea = input().split()
  I,V,X= int(linea[0]), int(linea[1]), int(linea[2])
  res = calcular(I, calcular(V,X))
  print((I+V+X)//res)
