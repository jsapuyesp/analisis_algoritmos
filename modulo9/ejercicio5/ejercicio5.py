def minFormula(x, total):
    return abs((2*x) - total)


def knapsack(monedasArr, total):
    totalColumnas = int(total/2)

    monedasLength = len(monedasArr)
    A = [[0 for __ in range(totalColumnas + 1)] for _ in range(monedasLength + 1)]

    for i in range(1, monedasLength + 1):
        prevIndex = i - 1
        monedaActual = monedasArr[prevIndex]
        for j in range(totalColumnas + 1):
            prevA = A[prevIndex][j]
            if(monedaActual <= j):

                x1 = A[prevIndex][j - monedaActual] + monedaActual
                x2 = A[prevIndex][j]
                fx1 = minFormula(x1, total)
                fx2 = minFormula(x2, total)
                A[i][j] = x1 if(fx1 <= fx2) else x2
            else:
                A[i][j] = prevA

    return A


def diferenciaMinima(arr):
    total = sum(arr)
    A = knapsack(arr, total)

    print(minFormula(A[-1][-1], total) * 10)


def main():
    casos = int(input())
    finalArr = []
    for _ in range(casos):
        finalArr.append([int(int(x) / 10) for x in input().split()])

    for arr in finalArr:
        diferenciaMinima(arr)


main()