import math 
alfa = 1
beta = 1

def palindromizar(text):
  global alfa
  global beta
  textInvert = text[::-1]
  matrizRange = len(text)+1
  P = [[math.inf for __ in range(0, matrizRange)] for _ in range(0, matrizRange)]

  for i in range(0, matrizRange):
    P[0][i] = alfa * i
    P[i][0] = alfa * i
  
  for i in range(1, matrizRange):
    prevI = i -1
    for j in range(1, matrizRange):
      prevJ = j -1
      prevValue = P[prevI][prevJ]
      x1 = prevValue + beta if(text[prevI] != textInvert[prevJ]) else prevValue
      x2 = P[i][prevJ] + alfa
      x3 = P[prevI][j] + alfa

      P[i][j] = min(x1,x2,x3)
  
  print(int(P[-1][-1]/2))

casos = int(input())
lista = []
for _ in range(0,casos):
  lista.append(input())

for text in lista:
  palindromizar(text)