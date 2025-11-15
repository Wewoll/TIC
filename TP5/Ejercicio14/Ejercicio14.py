import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils

prob_C1 = [0.7, 0.3]
matriz_canal_C1 = [
    [0.7, 0.3],
    [0.4, 0.6]
]

prob_C2 = [0.5, 0.5]
matriz_canal_C2 = [
    [0.3, 0.3, 0.4],
    [0.3, 0.3, 0.4]
]

prob_C3 = [0.25, 0.5, 0.25]
matriz_canal_C3 = [
    [1, 0, 0, 0],
    [0, 0.5, 0.5, 0],
    [0, 0, 0, 1],
]

prob_C4 = [0.25, 0.25, 0.25, 0.25]
matriz_canal_C4 = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 1, 0],
    [0, 0, 1]
]

probs_lista = [prob_C1, prob_C2, prob_C3, prob_C4]
matrices_lista = [matriz_canal_C1, matriz_canal_C2, matriz_canal_C3, matriz_canal_C4]
decimales = 4

for i, (prob_priori, matriz_canal) in enumerate(zip(probs_lista, matrices_lista), start=1):    
    print(f"\n--- Canal {i} ---")
    print(f"\na)")
    entropia_priori = utils.calculoEntropia(prob_priori)
    prob_salida = TP5_Funciones.calcularProbabilidadesSalida(prob_priori, matriz_canal)
    entropia_salida = utils.calculoEntropia(prob_salida)
    print(f"Entropia a Priori H(A):")
    utils.imprimirVector([entropia_priori], decimales)
    print(f"Entropia de salida H(B):")
    utils.imprimirVector([entropia_salida], decimales)

    print(f"\nb)")
    equivocacion = TP5_Funciones.calcularEquivocacion(prob_priori, matriz_canal)
    perdida = TP5_Funciones.calcularPerdida(prob_priori, matriz_canal)
    print(f"Equivocacion H(A|B):")
    utils.imprimirVector([equivocacion], decimales)
    print(f"Perdida H(B|A):")
    utils.imprimirVector([perdida], decimales)

    print(f"\nc)")
    entropia_afin = TP5_Funciones.calcularEntropiaAfin(prob_priori, matriz_canal)
    entropia_afin_relacion_1 = entropia_priori + perdida
    entropia_afin_relacion_2 = entropia_salida + equivocacion
    print(f"Entropia afin H(A, B):")
    utils.imprimirVector([entropia_afin], decimales)
    print(f"Entropia afin relacion H(A) + H(B|A):")
    utils.imprimirVector([entropia_afin_relacion_1], decimales)
    print(f"Entropia afin relacion H(B) + H(A|B):")
    utils.imprimirVector([entropia_afin_relacion_2], decimales)

    print(f"\nd)")
    informacion_mutua = TP5_Funciones.calcularInformacionMutua(prob_priori, matriz_canal)
    informacion_AB = entropia_priori - equivocacion
    informacion_BA = entropia_salida - perdida
    print(f"Informacion mutua H(A, B):")
    utils.imprimirVector([informacion_mutua], decimales)
    print(f"Entropia afin relacion H(A) - H(A|B):")
    utils.imprimirVector([informacion_AB], decimales)
    print(f"Entropia afin relacion H(B) - H(B|A):")
    utils.imprimirVector([informacion_BA], decimales)