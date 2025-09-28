import math

def calcInf(p):
    if p == 0:
        return 0
    return math.log2(1/p)

def calcEntropia(listaP):
    info = [calcInf(p) for p in listaP]
    return sum(a * b for a, b in zip(listaP, info))

listaW = [0.25, 0.75, 0.5, 1, 0]

for w in listaW:
  probW = w
  listaP = [probW, 1 - probW]
  print(f"Entropia = {calcEntropia(listaP):.2f}")