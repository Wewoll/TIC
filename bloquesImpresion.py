import utils

if True:
    probs_priori = []
    matriz_canal = [[]]
    matriz_canal_A = [[]]
    matriz_canal_B = [[]]
    decimales = 4


print("Probabilidades a Priori P(A):")
utils.imprimirVector(probs_priori, decimales)

print("Matriz del Canal P(B|A):")
utils.imprimirMatriz(matriz_canal, decimales)

probs_salida = utils.calcularProbabilidadesSalida(probs_priori, matriz_canal)
print("Probabilidades de Salida P(B):")
utils.imprimirVector(probs_salida, decimales)

matriz_simultanea = utils.calcularMatrizSimultanea(probs_priori, matriz_canal)
print("Matriz de Eventos Simultaneos P(A, B):")
utils.imprimirMatriz(matriz_simultanea, decimales)

matriz_posteriori = utils.calcularMatrizPosteriori(probs_priori, matriz_canal)
print("Matriz a Posteriori P(A|B):")
utils.imprimirMatriz(matriz_posteriori, decimales)

entropias_posteriori = utils.calcularEntropiasPosteriori(probs_priori, matriz_canal)
print("Entropias a Posteriori H(A|Bj):")
utils.imprimirEntropiasPosteriori(entropias_posteriori, decimales)

entropia_priori = utils.calculoEntropia(probs_priori)
print(f"Entropia a Priori H(A): {entropia_priori:.{decimales}f} bits")

entropia_salida = utils.calculoEntropia(probs_salida)
print(f"Entropia de Salida H(B): {entropia_salida:.{decimales}f} bits")

equivocacion = utils.calcularEquivocacion(probs_priori, matriz_canal)
print(f"Equivocacion H(A|B): {equivocacion:.{decimales}f} bits")

perdida = utils.calcularPerdida(probs_priori, matriz_canal)
print(f"Perdida H(B|A): {perdida:.{decimales}f} bits")

entropia_afin = utils.calcularEntropiaAfin(probs_priori, matriz_canal)
print(f"Entropia Afin H(A, B): {entropia_afin:.{decimales}f} bits")

informacion_mutua = utils.calcularInformacionMutua(probs_priori, matriz_canal)
print(f"Informacion Mutua I(A, B): {informacion_mutua:.{decimales}f} bits")

matriz_compuesta = utils.calcularMatrizCompuesta(matriz_canal_A, matriz_canal_B)
print("Matriz Compuesta P(C|A):")
utils.imprimirMatriz(matriz_compuesta)

capacidad = utils.calcularCapacidadEspecial(matriz_canal)
print(f"Capacidad (C): {capacidad:.{decimales}f} bits")

capacidad_estimada, probabilidad_optima = utils.estimarCapacidadCanalBinario(matriz_canal)
print(f"Capacidad estimada (C): {capacidad_estimada:.{decimales}f} bits")
print(f"Probabilidad optima (p): {probabilidad_optima:.{decimales}f}")

prob_error = utils.calcularProbabilidadError(probs_priori, matriz_canal)
print(f"Probabilidad de error (P_e): {prob_error:.{decimales}f}")