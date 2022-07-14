def knapstackMatriz(productosList, pesoMaximo):
  lenProductos = len(productosList)
  a = [[0 for __ in range(0,pesoMaximo+1)] for _ in range(0,lenProductos+1)]

  for i in range(1,lenProductos+1):
    preIndex = i - 1
    costoActual = productosList[preIndex][1]
    for j in range(0,pesoMaximo+1):
      prevA = a[preIndex][j]
      if (costoActual <= j):
        llega = productosList[preIndex][0]
        k = j - costoActual
        a[i][j] = max(llega+a[preIndex][k], prevA)
      else: a[i][j] = prevA
  return a

def maxPrecio(productosList : list, familiaArr : list, pesoMaxFamilia: int):
  a = knapstackMatriz(productosList, pesoMaxFamilia)
  s = 0
  for miembro in familiaArr:
    s += a[-1][miembro]
  print(s)

def main():
  numeroProductos = int(input())
  productosList = []
  for _ in range(0,numeroProductos):
    productosList.append([int(x) for x in input().split()])
  
  numeroFamilia = int(input())
  familiaArr = []
  pesoMaxFamilia = 0
  for _ in range(0, numeroFamilia):
    miembro = int(input())
    pesoMaxFamilia = max(miembro, pesoMaxFamilia)
    familiaArr.append(miembro)
  
  maxPrecio(productosList,familiaArr, pesoMaxFamilia)

main()