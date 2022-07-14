import heapq, math

def recorrido(coordenadas):
  grafo = {}
  primerCoordenada = coordenadas.pop()
  grafo['0'] = {
    'distancia' : 0,
    'x&y': primerCoordenada
  }

  pq = [None for _ in range(0, len(coordenadas))]
  idPendiente = []
  for i in range(0, len(coordenadas)):
    nId = i + 1
    coordActual = coordenadas[i]
    distancia = math.dist(primerCoordenada, coordActual)
    grafo[nId] = {
      'distancia' : distancia,
      'x&y' : coordActual
    }
    pq[i] = [distancia, nId]
    idPendiente.append(nId)
  
  heapq.heapify(pq)
  largoTotal = 0

  while(len(idPendiente) > 0):
    u = heapq.heappop(pq)
    uId = u[1]
    uNodo = grafo[uId]

    if (uId in idPendiente):
      idPendiente.remove(uId)
      largoTotal += uNodo['distancia']

      for id in idPendiente:
        vNodo = grafo[id]

        distancia = math.dist(uNodo['x&y'], vNodo['x&y'])
        distAct = vNodo['distancia']

        if(distancia < distAct):
          vNodo['distancia'] = distancia
          heapq.heappush(pq, [distancia, id])
  print(round(largoTotal, 1))


def main():
  casos = int(input())
  arr = []
  for _ in range(casos):
    nodos = int(input())
    arrCaso = []
    for __ in range(nodos):
      arrCaso.append([float(x) for x in input().split()])
    arr.append(arrCaso)
  
  for i in arr:
    recorrido(i)


main()