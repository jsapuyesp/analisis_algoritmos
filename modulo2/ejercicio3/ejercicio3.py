import math 

casos = int(input())

def primo(x):
  if x==2: return True
  for i in range(2, math.ceil(math.sqrt(x))+1):
    if x%i==0: return False
  return True

for i in range(0, casos):
  x,y = input().split()
  x,y = int(x), int(y)
  contador = 0
  for j in range (x, y+1):
    if primo(j):
      contador += 1
  print(contador)
    


