modulo= 999999937

def fibonacci(a,b,c,d,N):
  global modulo
  if(N==1):
    return 1,1,1,0
  elif(N%2==0):
    a1,b1,c1,d1 = fibonacci(a,b,c,d,N/2)
    tupla1 = (a1 * a1) + (b1 * c1)
    tupla2 = b1 * (a1 + d1)
    tupla3 = c1 * (a1 + d1)
    tupla4 = (d1 * d1) + (b1 * c1)
    return tupla1%modulo,tupla2%modulo,tupla3%modulo,tupla4%modulo
  else:
    a1,b1,c1,d1 = fibonacci(a,b,c,d,(N-1)/2)
    tupla1 = (a1 * a1) + (b1 * c1) + b1*(a1 + d1)
    tupla2 = (a1 * a1) + (b1 * c1)
    tupla3 = c1 * (a1 + d1) + (d1 * d1) + (b1 * c1)
    tupla4 = c1 * (a1 + d1)
    return tupla1%modulo,tupla2%modulo,tupla3%modulo,tupla4%modulo


def getNum(n):
  global modulo
  a1,b1,c1,d1 = fibonacci(1,1,1,0,n)
  print(d1)



casos = int(input())

for _ in range(0,casos):
  entrada = int(input())
  getNum(entrada)
  