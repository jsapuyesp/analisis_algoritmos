casos = int(input())
for i in range(0,casos):
  lista = [int(x) for x in input().split()]
  listaLen = lista[0]
  lista = lista[1:]

  o1 = [lista[0] if i==0 else None for i in range(0,listaLen)]
  o2 = [lista[0] if i==0 else None for i in range(0,listaLen)]

  for i in range(0,listaLen):

    o1[i] = lista[i]
    o2[i] = lista[i]
    
    for j in range(0,i):
      listaJ = lista[j]

      pendientes = i-j-1

      o1[i] = min(o1[i], listaJ + o1[pendientes])
      o2[i] = max(o2[i], listaJ + o2[pendientes])
  
  print(str(o1[-1])+' '+str(o2[-1]))