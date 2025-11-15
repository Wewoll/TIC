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
i = 0
decimales = 4

for canal in canales:
    i += 1
    prob_priori = utils.genProbabilidadesAlf(canal[0])
    matriz_canal = TP5_Funciones.genMatrizCanal(canal[0], canal[1])

    matriz_posteriori = TP5_Funciones.calcularMatrizPosteriori(prob_priori, matriz_canal)
    matriz_simultaneos = TP5_Funciones.calcularMatrizSimultanea(prob_priori, matriz_canal)
    
    print(f"\n--- Canal {i} ---")
    print("Probabilidades a posteriori:")
    utils.imprimirMatriz(matriz_posteriori, decimales)
    
    print("Probabilidades de los eventos simultaneos:")
    utils.imprimirMatriz(matriz_simultaneos, decimales)