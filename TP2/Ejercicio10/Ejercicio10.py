import itertools

# Generar alfabeto y probabilidades
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

def genListasOrdN(alfabeto, probabilidades, N):
    # Generar alfabeto extendido
    alfabetoN = ["".join(tupla) for tupla in itertools.product(alfabeto, repeat=N)]
    
    # Generar probabilidades extendidas
    probabilidadesN = []
    for tupla in itertools.product(range(len(alfabeto)), repeat=N):
        p = 1
        for i in tupla:
            p *= probabilidades[i]
        probabilidadesN.append(p)
    
    return alfabetoN, probabilidadesN

# --- Ejemplo de uso ---
cadena_original = "ABCBBCABCBCACC"
N = 3

# Lista alfabeto y lista probabilidades
alfabeto, probabilidades = genListas(cadena_original)
print(f"Alfabeto: {alfabeto}")
print(f"Probabilidades: [{', '.join(f'{p:.2f}' for p in probabilidades)}]")

# Listas de extension de orden N
alfabetoN, probabilidadesN = genListasOrdN(alfabeto, probabilidades, N)
print(f"Alfabeto de orden {N}: {alfabetoN}")
print(f"Probabilidades de orden {N}: [{', '.join(f'{p:.2f}' for p in probabilidadesN)}]")