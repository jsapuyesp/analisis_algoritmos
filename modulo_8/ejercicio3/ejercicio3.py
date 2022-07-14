def karatsuba(n, n1, n2):
  if (n==1):
    resultado = int(n1)*int(n2)
    print(resultado)
    return str(resultado)
  else: 
    mitad = int(n/2)
    a = n1[:mitad]
    b = n1[mitad:]
    c = n2[:mitad]
    d = n2[mitad:]

    P1 = int(karatsuba(mitad, a, c))
    P2 = int(karatsuba(mitad, a, d))
    P3 = int(karatsuba(mitad, b, c))
    P4 = int(karatsuba(mitad, b, d))

    resultado = ((10**n)*P1) + ((10**mitad)*(P2 + P3)) + P4

    print(resultado)
    return str(resultado)

casos = int(input())
array = []
cont = 1
for _ in range(0, casos):
  arr = [x for x in input().split()]
  array.append([cont, arr])
  cont += 1

for i in range(len(array)):
  item = array[i]
  print("caso "+str(item[0])+":")
  n = int(item[1][0])
  n1 = item[1][1]
  n2 = item[1][2]
  karatsuba(n,n1,n2)
  if(i != casos - 1):
    print("")