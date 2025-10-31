import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

cadena_1 = "ABCDABCBDCBAAABBBCBCBABADBCBABCBDBCCCAAABB"
cadena_2 = "AOEAOEOOOOEOAOEOOEOOEOAOAOEOEUUUIEOEOEO"
cadenas = [cadena_1, cadena_2]
i = 64

for cadena in cadenas:
    i += 1
    alfabeto = utils.genAlfabeto(cadena)
    probabilidades = utils.genProbabilidadesAlf(cadena)
    huffman = TP4_Funciones.algoritmoHuffman(probabilidades)
    shannon_fano = TP4_Funciones.algoritmoHuffman(probabilidades)
    longitudes = utils.genLongitudesCodigos(huffman)
    print(f"\n{chr(i)}.")
    print(f"S = {alfabeto}")
    print(f"P = [{', '.join(f'{p:.2f}' for p in probabilidades)}]")
    print(f"L = {longitudes}")
    print(f"Huffman: {huffman}")
    print(f"Shannon-Fano: {shannon_fano}")