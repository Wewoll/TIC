import math

listaP = [1/9, 1/6, 1/9, 1/9, 1/6, 1/3]

def calcInf(p):
    return math.log2(1/p)

def calcEntropia(listaP):
    info = [calcInf(p) for p in listaP]
    return sum(a * b for a, b in zip(listaP, info))

# listaI = [calcInf(p) for p in listaP]
print([calcInf(p) for p in listaP])

print(calcEntropia(listaP))