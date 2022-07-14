def caminos(lista):
  denominaciones = [1,2,5,10,20,50,100]
  denominacionesLen = len(denominaciones)
  maxItem = max(lista) + 1
  M = [[1 for __ in range(maxItem)] for _ in range(denominacionesLen)]

  for i in range(1, denominacionesLen):
    for j in range(0, maxItem):
      prevItem = M[i - 1][j]
      if (j < denominaciones[i]):
        M[i][j] = prevItem
      else:
        M[i][j] = prevItem + M[i][j-denominaciones[i]]
  
  for n in lista:
    print(M[-1][n])

def main():
  lista = []
  while True:
    n = int(input())
    if(n==0):
      break
    lista.append(n)
  caminos(lista)

main()
