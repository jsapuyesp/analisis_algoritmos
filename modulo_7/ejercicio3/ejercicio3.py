import heapq

contador = 0

def union(izquierda, derecha, largo):
  global contador
  i = 0
  j = 0
  k = 0
  auxLista = []
  largoI = len(izquierda)
  largoD = len(derecha)

  while k < largo:
    if(i<largoI):
      if(j<largoD):
        if(izquierda[i]<=derecha[j]):
          auxLista.append(izquierda[i])
          i += 1
        else:
          auxLista.append(derecha[j])
          contador += (largoI - i)
          j += 1
      else:
        auxLista.extend(izquierda[i:])
        break
    else:
      if(j < largoD):
        auxLista.extend(derecha[j:])
        break
    k += 1
  return auxLista

def ordenamiento(lista):
  if len(lista)>1:
    medio = len(lista)//2
    izquierda = lista[:medio]
    derecha = lista[medio:]
    return union(ordenamiento(izquierda),ordenamiento(derecha), len(lista))
  
  else:
    return lista

def imperfeccionScore(e):
  arr = []
  for char in e:
    arr.append(char)
  ordenamiento(arr)

def mejor(lista, e):
  global contador
  pq = []
  heapq.heapify(pq)
  for element in lista:
    imperfeccionScore(element)
    criterioArr = [contador, element]
    heapq.heappush(pq, criterioArr)
    contador = 0
  
  for _ in range(e):
    elementoElegido = heapq.heappop(pq)
    print(elementoElegido[1])

def main():
  entrada = input().split()
  totalElementos = int(entrada[0])
  eleccion = int(entrada[1])

  arrFinal = []
  for _ in range(0, totalElementos):
    arrFinal.append(input())

  mejor(arrFinal, eleccion)

main()
