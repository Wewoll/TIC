import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils

prob_C1 = [2/5, 3/5]
prob_C2 = [3/4, 1/4]

matriz_canal_C1 = [
    [3/5, 2/5],
    [1/3, 2/3]
]

matriz_canal_C2 = [
    [2/3, 1/3],
    [1/10, 9/10]
]

probs_lista = [prob_C1, prob_C2]
matrices_lista = [matriz_canal_C1, matriz_canal_C2]
decimales = 4

for i, (probs, matriz_canal) in enumerate(zip(probs_lista, matrices_lista), start=1):
    print(f"\n--- Canal {i} ---")
    
    entropia_priori = utils.calculoEntropia(probs)
    print(f"Entropía a Priori H(A):")
    utils.imprimirVector([entropia_priori], decimales)

    lista_entropias_post = TP5_Funciones.calcularEntropiasPosteriori(probs, matriz_canal)
    print(f"Entropías a Posteriori H(A|Bj):")
    utils.imprimirVector(lista_entropias_post, decimales)
    