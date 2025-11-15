import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP5_Funciones
import utils

canal1_entrada = "1101011001101010010101010100011111"
canal1_salida = "1001111111100011101101010111110110"
canal1 = [canal1_entrada, canal1_salida]

canal2_entrada = "110101100110101100110101100111110011"
canal2_salida = "110021102110022010220121122100112011"
canal2 = [canal2_entrada, canal2_salida]

canales = [canal1, canal2]
i = 0

for canal in canales:
    i += 1
    prob_apriori = utils.genProbabilidadesAlf(canal[0])
    matriz_canal = TP5_Funciones.genMatrizCanal(canal[0], canal[1])
    print(f"\nCanal {i}:")

    probs_str = ", ".join([f"{p:.2f}" for p in prob_apriori])
    print(f"Probabilidades a priori: [ {probs_str} ]")

    print("Matriz del canal:")
    for fila in matriz_canal:
        fila_str = " | ".join([f"{prob:^6.2f}" for prob in fila])
        print(f"  [ {fila_str} ]")