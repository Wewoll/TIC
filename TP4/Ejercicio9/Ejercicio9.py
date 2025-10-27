import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

simbolos = ["S1", "S2", "S3", "S4"]
fuenteA = [0.2, 0.2, 0.3, 0.3]
fuenteB = [0.4, 0.25, 0.25, 0.1]

fuentes = [fuenteA, fuenteB]
i = 64

for probs in fuentes:
    i += 1
    cod_huffman = TP4_Funciones.algoritmoHuffman(probs)
    cod_shannon_fano = TP4_Funciones.algoritmoShannonFano(probs)
    long_huffman = utils.genLongitudesCodigos(cod_huffman)
    long_shannon_fano = utils.genLongitudesCodigos(cod_shannon_fano)
    print(f"Huffman: L{chr(i)} = {long_huffman}\tShannon-Fano: L{chr(i)} = {long_shannon_fano}")