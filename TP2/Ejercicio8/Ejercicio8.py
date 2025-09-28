import math

def calcInf(p):
    return math.log2(1/p)

def calcEntropia(listaP):
    info = [calcInf(p) for p in listaP]
    return sum(a * b for a, b in zip(listaP, info))

probW = float(input("Introduce un valor w: "))
listaP = [probW, 1 - probW]

print(f"Entropia = {calcEntropia(listaP):.2f}")