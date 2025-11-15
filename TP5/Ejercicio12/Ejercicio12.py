import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils

canal1_entrada = "abcacaabbcacaabcacaaabcaca"
canal1_salida  = "01010110011001000100010011"
canal1 = [canal1_entrada, canal1_salida]

canal3_1_entrada = "1101011001101010010101010100011111"
canal3_1_salida = "1001111111100011101101010111110110"
canal3_1 = [canal3_1_entrada, canal3_1_salida]

canal3_2_entrada = "110101100110101100110101100111110011"
canal3_2_salida = "110021102110022010220121122100112011"
canal3_2 = [canal3_2_entrada, canal3_2_salida]

canales = [canal1, canal3_1, canal3_2]

probs_lista = []
matrices_lista = []

for canal in canales:
    prob_priori = utils.genProbabilidadesAlf(canal[0])
    matriz_canal = TP5_Funciones.genMatrizCanal(canal[0], canal[1])

    probs_lista.append(prob_priori)
    matrices_lista.append(matriz_canal)
    
prob_A_6 = [0.3, 0.3, 0.4]
matriz_canal_6 = [
    [0.4, 0.4, 0.2],
    [0.3, 0.2, 0.5], 
    [0.3, 0.4, 0.3]
]

probs_lista.append(prob_A_6)
matrices_lista.append(matriz_canal_6)

decimales = 4

for i, (probs, matriz_canal) in enumerate(zip(probs_lista, matrices_lista), start=1):
    print(f"\n--- Canal {i} ---")
    
    entropia_priori = utils.calculoEntropia(probs)
    print(f"Entropía a Priori H(A):")
    utils.imprimirVector([entropia_priori], decimales)

    lista_entropias_post = TP5_Funciones.calcularEntropiasPosteriori(probs, matriz_canal)
    print(f"Entropías a Posteriori H(A|Bj):")
    utils.imprimirVector(lista_entropias_post, decimales)