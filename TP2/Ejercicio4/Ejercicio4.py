import math

def calcInf(p):
    """Cantidad de información en bits de un símbolo con prob p."""
    if p == 0:
        return float('inf')   # Convención: infinito si p=0
    return -math.log2(p)

def calcEntropia(probs):
    """Entropía Shannon: H = -Σ p*log2(p)."""
    return sum(p * calcInf(p) for p in probs if p > 0)

def procesar_fuente(alfabeto, probs, nombre=None, decimals=2):
    """Muestra información por símbolo y entropía de una fuente."""
    if len(alfabeto) != len(probs):
        raise ValueError("Alfabeto y probabilidades deben tener la misma longitud.")
    if not math.isclose(sum(probs), 1.0, rel_tol=1e-9):
        raise ValueError(f"Las probabilidades suman {sum(probs)}, no 1.")

    info = [calcInf(p) for p in probs]
    H = calcEntropia(probs)

    title = f"Fuente: {nombre}" if nombre else "Fuente"
    print("=" * 40)
    print(title)
    print("-" * 40)
    print(f"{'Símbolo':>7} | {'P(s)':>6} | {'I(s) [bits]':>12}")
    print("-" * 40)
    for s, p, i in zip(alfabeto, probs, info):
        i_str = f"{i:.{decimals}f}" if not math.isinf(i) else "inf"
        print(f"{repr(s):>7} | {p:6.{decimals}f} | {i_str:>12}")
    print("-" * 40)
    print(f"Entropía H = {H:.{decimals}f} bits")
    print("=" * 40)
    print()

# Definimos las tres fuentes del enunciado
fuentes = [
    (["x","y","z"], [0.5, 0.1, 0.4], "Fuente xyz"),
    (["0","1"], [0.5, 0.5], "Fuente binaria"),
    (["A","B","C","D"], [0.1, 0.3, 0.4, 0.2], "Fuente ABCD"),
]

# Procesar todas
for alfabeto, probs, nombre in fuentes:
    procesar_fuente(alfabeto, probs, nombre)