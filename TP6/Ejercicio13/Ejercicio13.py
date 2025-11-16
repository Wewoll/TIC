import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils

matriz_canal = [
    [0.6, 0.3, 0.1],
    [0.1, 0.8, 0.1],
    [0.3, 0.3, 0.4]
]

probs_priori_A = [1/3, 1/3, 1/3]
probs_priori_B = [1/8, 3/8, 4/8]
probs_priori_C = [4/15, 3/15, 8/15]

probs_lista = [probs_priori_A, probs_priori_B, probs_priori_C]
decimales = 4

for i, probs_priori in enumerate(probs_lista, start=1):
    print(f"\nCanal {i}:")
    prob_error = TP6_Funciones.calcularProbabilidadError(probs_priori, matriz_canal)
    print(f"Probabilidad de error (P_e): {prob_error:.{decimales}f}")