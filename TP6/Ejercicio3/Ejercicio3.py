import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils

probs_A = [1/2, 1/2]
matriz_canal_A = [
    [0.7, 0, 0.3, 0],
    [0.2, 0.6, 0, 0.2]
]

probs_B = utils.calcularProbabilidadesSalida(probs_A, matriz_canal_A)
matriz_canal_B = [
    [0.9, 0, 0.1],
    [0, 1, 0],
    [0.1, 0.1, 0.8],
    [0, 0.5, 0.5]
]

decimales = 4

print(f"\na)")
print(f"\n--- Canal A ---")
equivocacion = utils.calcularEquivocacion(probs_A, matriz_canal_A)
print(f"Equivocacion H(A|B): {equivocacion:.{decimales}f}")
informacion_mutua = utils.calcularInformacionMutua(probs_A, matriz_canal_A)
print(f"Informacion Mutua I(A, B): {informacion_mutua:.{decimales}f}")

print(f"\n--- Canal B ---")
equivocacion = utils.calcularEquivocacion(probs_B, matriz_canal_B)
print(f"Equivocacion H(B|C): {equivocacion:.{decimales}f}")
informacion_mutua = utils.calcularInformacionMutua(probs_B, matriz_canal_B)
print(f"Informacion Mutua I(B, C): {informacion_mutua:.{decimales}f}")

print(f"\nb)")
matriz_compuesta = TP6_Funciones.calcularMatrizCompuesta(matriz_canal_A, matriz_canal_B)
print(f"Matriz compuesta P(C|A):")
utils.imprimirMatriz(matriz_compuesta)

print(f"\nc)")
equivocacion = utils.calcularEquivocacion(probs_A, matriz_compuesta)
print(f"Equivocacion H(A|C): {equivocacion:.{decimales}f}")
informacion_mutua = utils.calcularInformacionMutua(probs_A, matriz_compuesta)
print(f"Informacion Mutua I(A, C): {informacion_mutua:.{decimales}f}")