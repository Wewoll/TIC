import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils

prob_C1 = [0.14, 0.52, 0.34]
matriz_canal_C1 = [
    [0.50, 0.30, 0.20],
    [0.00, 0.40, 0.60],
    [0.20, 0.80, 0.00]
]

prob_C2 = [0.25, 0.25, 0.50]
matriz_canal_C2 = [
    [0.25, 0.25, 0.25, 0.25],
    [0.25, 0.25, 0.00, 0.50],
    [0.50, 0.00, 0.50, 0.00]
]

prob_C3 = [0.12, 0.24, 0.14, 0.50]
matriz_canal_C3 = [
    [0.25, 0.15, 0.30, 0.30],
    [0.23, 0.27, 0.25, 0.25],
    [0.10, 0.40, 0.25, 0.25],
    [0.34, 0.26, 0.20, 0.20]
]

probs_lista = [prob_C1, prob_C2, prob_C3]
matrices_lista = [matriz_canal_C1, matriz_canal_C2, matriz_canal_C3]
decimales = 4

for i, (probs, matriz_canal) in enumerate(zip(probs_lista, matrices_lista), start=1):
    print(f"\n--- Canal {i} ---")
    
    entropia_priori = utils.calculoEntropia(probs)
    print(f"Entropía a Priori H(A): {entropia_priori:.4f}")

    lista_entropias_post = TP5_Funciones.calcularEntropiasPosteriori(probs, matriz_canal)
    print(f"Entropías a Posteriori H(A|bj):")
    utils.imprimirEntropiasPosteriori(lista_entropias_post)