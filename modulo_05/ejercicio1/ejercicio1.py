

casos = int(input())

for __ in range(0,casos):
  ninos = int(input())
  orden = [False]*ninos
  lista_tuplas = []
  for _ in range(0,ninos):
    linea = input().split()
    map_linea = map(int, linea)
    lista_int = list(map_linea)
    tupla = tuple(lista_int)
    lista_tuplas.append(tupla)
  lista_tuplas.sort(key = lambda x: x[1], reverse= True)
  
  q = ninos-1
  pataleta = 0

  for i in range(0, ninos):
    nino = lista_tuplas[i]
    p = int(nino[0]/10)
    while(orden[p]!=False):
      p-=1
    if(p>=0):
      orden[p]=True
    else:
      while(orden[q]!=False):
        q-=1
      orden[q]=True
      pataleta += nino[1]
      q-=1
  print(pataleta)