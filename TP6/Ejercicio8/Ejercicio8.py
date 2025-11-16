import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils

prob_C1 = [1/4, 1/4, 1/4, 1/4]
matriz_canal_C1 = [
    [0, 1, 0],
    [0, 0, 1],
    [0, 1, 0],
    [1, 0, 0]
]

prob_C2 = [1/3, 1/3, 1/3]
matriz_canal_C2 = [
    [1, 0, 0, 0],
    [0, 0.2, 0, 0.8],
    [0, 0, 1, 0]
]

prob_C3 = [1/3, 1/3, 1/3]
matriz_canal_C3 = [
    [0.3, 0.5, 0.2],
    [0.2, 0.3, 0.5],
    [0.5, 0.2, 0.3]
]

prob_C4 = [1/4, 1/4, 1/4, 1/4]
matriz_canal_C4 = [
    [0, 0, 1, 0],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 1]
]

probs_lista = [prob_C1, prob_C2, prob_C3, prob_C4]
matrices_lista = [matriz_canal_C1, matriz_canal_C2, matriz_canal_C3, matriz_canal_C4]

for i, (prob_priori, matriz_canal) in enumerate(zip(probs_lista, matrices_lista), start=1):
    print(f"\n--- Canal {i} ---")

    capacidad = TP6_Funciones.calcularCapacidadEspecial(matriz_canal)
    print(f"Capacidad (C): {capacidad:.4f} bits")