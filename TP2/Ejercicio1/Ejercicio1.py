import math

listaP = [0.15, 0.25, 0.5, 0.05, 0.05]

def calcInf(p):
    return math.log2(1/p)

def calcEntropia(listaP):
    info = [calcInf(p) for p in listaP]
    return sum(a * b for a, b in zip(listaP, info))

# listaI = [calcInf(p) for p in listaP]
print([calcInf(p) for p in listaP])

print(calcEntropia(listaP))