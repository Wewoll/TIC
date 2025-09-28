import math

def genListas(cadena):
    listaA = []
    listaP = []
    for letter in cadena:
        if letter in listaA:
            listaP[listaA.index(letter)] += 1
        else:
            listaA.append(letter)
            listaP.append(1)

    total = sum(listaP)
    listaP = [f / total for f in listaP]  # pasar a probabilidades
    return listaA, listaP

def calcInf(p):
    return math.log2(1/p)

def calcEntropia(listaP):
    info = [calcInf(p) for p in listaP]
    return sum(a * b for a, b in zip(listaP, info))

cadena_original = "ABDAACAABACADAABDAADABDAAABDCDCDCDC"

# 2a
alfabeto, probabilidades = genListas(cadena_original)
entropia = calcEntropia(probabilidades)
print("Alfabeto:", alfabeto)
print("Probabilidades:", probabilidades)
print("Entropia: ", entropia)