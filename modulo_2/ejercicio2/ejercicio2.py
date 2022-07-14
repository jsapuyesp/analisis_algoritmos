import math

casos = int(input())

for i in range(0, casos):
  cantidad = int(input())
  divisores= 2
  for j in range(2,int(math.ceil(math.sqrt(cantidad)))+1):
    if cantidad%j == 0: 
      if j != cantidad/j:
        divisores+=1
      divisores+=1
  print(divisores)
