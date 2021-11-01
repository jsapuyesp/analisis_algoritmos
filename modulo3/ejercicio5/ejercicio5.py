def coloresValidos(c, n, lista, s, matriz):
    if n == s:
        for i in lista:
            _sirve = True
            for j in range(n - 1):
                for k in range(j + 1, n):
                    if lista[j] == lista[k] and matriz[j][k]:
                        _sirve = False
                        break
                if not _sirve:
                    break
            if _sirve:
                return True
            return False
    else:
        for i in range(c):
            if coloresValidos(c, n, lista + [i], s + 1, matriz):
                return True


casos = int(input())
for i in range(0,casos):
    n = int(input())
    matriz = []
    for j in range(0,n):
        linea = input().split()
        lineaAux = [int(x) for x in linea]
        matriz.append(lineaAux)
    res = n
    for j in range(1, n):
        if coloresValidos(j, n, [], 0, matriz):
            res = j
            break
    print(res)