def strassen(n, m1, m2):
    if(n == 2):
        a = m1[0][0]
        b = m1[0][1]
        c = m1[1][0]
        d = m1[1][1]

        e = m2[0][0]
        f = m2[0][1]
        g = m2[1][0]
        h = m2[1][1]

        sum =  a*e + b*g + a*f + b*h + c*e + d*g + c*f + d*h
        print(sum)
        return sum
    else:
        mitad = int(n / 2)

        A = [x[:mitad] for x in m1[:mitad]]
        B = [x[mitad:] for x in m1[:mitad]]
        C = [x[:mitad] for x in m1[mitad:]]
        D = [x[mitad:] for x in m1[mitad:]]

        E = [x[:mitad] for x in m2[:mitad]]
        F = [x[mitad:] for x in m2[:mitad]]
        G = [x[:mitad] for x in m2[mitad:]]
        H = [x[mitad:] for x in m2[mitad:]]


        P1 = strassen(mitad, A, E)
        P2 = strassen(mitad, B, G)
        P3 = strassen(mitad, A, F)
        P4 = strassen(mitad, B, H)
        P5 = strassen(mitad, C, E)
        P6 = strassen(mitad, D, G)
        P7 = strassen(mitad, C, F)
        P8 = strassen(mitad, D, H)


        sum = P1 + P2 + P3 + P4 + P5 + P6 + P7 + P8

        print(sum)
        return sum



array = []
casos = int(input())
for _ in range(casos):
    n = int(input())
    m1 = []
    m2 = []
    for __ in range(n):
        m1.append([int(x) for x in input().split()])
    for __ in range(n):
        m2.append([int(x) for x in input().split()])
    array.append([n, m1, m2])

for i in range(casos):
    casoArr = array[i]
    print("caso "+str(i+1)+":")
    strassen(casoArr[0], casoArr[1], casoArr[2])
    if(i != casos - 1):
        print("")


