import math 
S = []
luces = []

def getSum(x):
  s = 0
  for i in x:
    s += i[1]
  return s

def arbol(i,j, nivel: int=0):
  global S
  global luces

  raiz = S[i][j]

  if (raiz < j):
    arbol(raiz+1, j, nivel+1)
  print('\t'*nivel + luces[raiz][0])

  if i < raiz:
    arbol(i, raiz-1, nivel+1)

def getArbol():
  global luces
  global S
  lenLuces = len(luces)
  C = [[0 for __ in range(lenLuces)] for _ in range(lenLuces)]
  S = [[0 for __ in range(lenLuces)] for _ in range(lenLuces)]

  for i in range(0, lenLuces):
    C[i][i] = luces[i][1]

  for nodo in range(1, lenLuces + 1):
    for i in range(0, lenLuces-nodo + 1):
      j = i+nodo-1
      lowest = math.inf
      actSum = getSum(luces[i:j+1])
      for r in range(i,j+1):
        r1 = r - 1
        r2 = r + 1
        item1 = 0 if r1 < 0 else C[i][r1]
        item2 = 0 if r2 >= lenLuces else C[r2][j]
        expr = item1 + item2 + actSum
        if(expr < lowest):
          lowest = expr
          S[i][j] = r
      C[i][j]= lowest
  arbol(0, lenLuces-1)


def main():
  global luces
  
  casos = int(input())
  lista = []

  for _ in range(0, casos):
    caso = []
    for i in input().split():
      item = i.split(':')
      caso.append([item[0], int(item[1])])
    lista.append(caso)
  
  finalIndex = len(lista)-1

  for i in range(0, len(lista)):
    print(f"caso {i + 1}:")
    print("")
    luces = lista[i]
    luces.sort()
    getArbol()
    if(i != finalIndex):
      print('')

main()