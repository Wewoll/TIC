import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

probabilidades = [0.385, 0.154, 0.128, 0.154, 0.179]

huffman = TP4_Funciones.algoritmoHuffman(probabilidades)
shannon_fano = TP4_Funciones.algoritmoShannonFano(probabilidades)
rendimiento_huffman, redundancia_huffman = TP4_Funciones.calculoRendimientoYRedundancia(huffman, probabilidades)
rendimiento_shannon_fano, redundancia_shannon_fano = TP4_Funciones.calculoRendimientoYRedundancia(shannon_fano, probabilidades)

print(f"a. Entropia: {utils.calculoEntropia(probabilidades):.4f}")
print(f"b. Huffman: {huffman}\t L: {utils.genLongitudesCodigos(huffman)}")
print(f"c. Shannon-Fano: {shannon_fano}\t L: {utils.genLongitudesCodigos(shannon_fano)}")
print(f"e.")
print(f"Huffman:\tL: {utils.calculoLongitudMedia(huffman, probabilidades):.4f} bits\tη: {rendimiento_huffman:.4f}\tR: {redundancia_huffman:.4f}")
print(f"Shannon-Fano:\tL: {utils.calculoLongitudMedia(shannon_fano, probabilidades):.4f} bits\tη: {rendimiento_shannon_fano:.4f}\tR: {redundancia_shannon_fano:.4f}")