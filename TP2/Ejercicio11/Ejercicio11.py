import itertools
import math

# --- Funciones ---
def calcInf(p):
    return math.log2(1/p) if p > 0 else 0  # evitar log(0)

def calcEntropia(listaP):
    info = [calcInf(p) for p in listaP]
    return sum(a * b for a, b in zip(listaP, info))

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

# --- Fuentes del ejercicio 4 ---
fuentes = [
    (["x","y","z"], [0.5, 0.1, 0.4], "Fuente xyz"),
    (["0","1"], [0.5, 0.5], "Fuente binaria"),
    (["A","B","C","D"], [0.1, 0.3, 0.4, 0.2], "Fuente ABCD"),
]

# --- Generar extensiones y calcular entropías ---
for alfabeto, probabilidades, nombre in fuentes:
    print(f"\n--- {nombre} ---")
    H_S = calcEntropia(probabilidades)  # entropía de la fuente original
    print(f"H(S) = {H_S:.2f}")
    
    for N in [2, 3]:
        alfabetoN, probabilidadesN = genListasOrdN(alfabeto, probabilidades, N)
        H_SN = calcEntropia(probabilidadesN)
        print(f"\nExtensión de orden {N}:")
        print(f"H(S^{N}) = {H_SN:.2f}")
        print(f"Comprobación: n * H(S) = {N*H_S:.2f}")
        print(f"Verificación: {'OK' if abs(H_SN - N*H_S) < 1e-6 else 'Error'}")