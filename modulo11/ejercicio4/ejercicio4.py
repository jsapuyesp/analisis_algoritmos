import math
S = []
resultado = ''

def getParentesis(i,j):
  global resultado
  if(i == j):
    resultado += f'M'
  else: 
    resultado += '('
    getParentesis(i, S[i][j])
    getParentesis(1+S[i][j], j)
    resultado += ')'

def multiplicacion(lista):
  global S
  global resultado
  listaLen = len(lista)
  M = [[0 for __ in range(listaLen)] for _ in range(listaLen)]
  S = [[0 for __ in range(listaLen)] for _ in range(listaLen)]


  for matriz in range(1,listaLen):
    for i in range(0, listaLen-matriz):
      j = i + matriz
      min = math.inf
      for k in range(i,j):
        item1 = M[i][k]
        item2 = M[k + 1][j]
        item3 = lista[i-1]*lista[k]*lista[j]
        Q = item1 + item2 + item3
        if(Q < min):
          min = Q
          S[i][j] = k
      M[i][j] = min
  
  resultado = ''
  getParentesis(1, listaLen - 1)
  resultado = resultado.replace('MM', "M x M")
  resultado = resultado.replace('M(', "M x (")
  resultado = resultado.replace(')M', ") x M")
  resultado = resultado.replace(')(', ") x (")

  final = ''

  resultadoArr = resultado.split('M')
  ultimoIndex = len(resultadoArr) - 1
  for i in range(0, len(resultadoArr)):
    if(i != ultimoIndex):
      final += f"{resultadoArr[i]}M{i + 1}"
    else:
      final += resultadoArr[i]
  print(final)

def main():
  casos = int(input())
  lista = []
  for _ in range(0,casos):
    lista.append([int(x) for x in input().split()])
  
  for item in lista:
    multiplicacion(item)

main()

