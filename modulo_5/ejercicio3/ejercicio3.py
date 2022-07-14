import heapq
n = int(input())
while n != 0:
    aux = []
    heapq.heapify(aux)
    for _ in range(n):
        heapq.heappush(aux, int(input()))
    costo = 0
    while len(aux) > 1:
        x = heapq.heappop(aux)
        y = heapq.heappop(aux)
        costo += x + y
        heapq.heappush(aux, x + y)
    print(costo)
    n = int(input())