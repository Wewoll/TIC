# ÍNDICE DE FUNCIONES (TIC - 2025)

## --- TP 2: FUENTES DE INFORMACIÓN ---
* `calculoInformacion(p, base=2)` -> float
* `calculoEntropia(probabilidades, base=2)` -> float
* `genAlfabeto(cadena)` -> list
* `genProbabilidadesAlf(cadena)` -> list
* `genMensaje(alfabeto, probabilidades, longitud_msj=20)` -> str
* `calculoEntropiaBin(probW, base=2)` -> float
* `genAlfabetoOrdN(alfabeto, N)` -> list
* `genProbabilidadesAlfOrdN(probabilidades, N)` -> list
* `itertools_GenListasOrdN(alfabeto, probabilidades, N)` -> (list, list)
* `genVectorEstacionario(matriz, tol=0.01, iter=500)` -> list
* `maxDifVec(vector_ant, vector_nuevo)` -> float
* `calculoEntropiaMarkov(matriz, base=2)` -> float
* `genMatrizTransicion(cadena)` -> list[list] (Llama a Ocurrencias y Probabilidades)
* `genMatrizOcurrencias(cadena)` -> list[list]
* `genMatrizProbabilidades(matriz_ocurrencias)` -> list[list]
* `genMensajeMarkov(alfabeto, matriz, longitud_msj=20, estado_inicial=None)` -> str
* `esFuenteSinMemoria(matriz, tolerancia)` -> bool
* `esFuenteErgodica(matriz)` -> bool

## --- TP 3: CÓDIGOS ---
* `esNoSingular(codigos)` -> bool
* `esNoSingularFor(codigos)` -> bool
* `esInstantaneo(codigos)` -> bool
* `esUnivoco(codigos)` -> bool
* `tipoCodigo(codigos)` -> str ("Instantáneo", "Unívoco", "No singular", "Bloque")
* `calculoInecuacionKraft(codigos)` -> float
* `calculoInformacionR(p, r)` -> float
* `calculoEntropiaCP(codigos, probabilidades)` -> float
* `calculoLongitudMedia(codigos, probabilidades)` -> float
* `calculoLongitudIdeal(probabilidades, r)` -> list[int]
* `esCodigoCompacto(codigos, probabilidades)` -> bool
* `genMensajeCP(codigos, probabilidades, N)` -> str

## --- TP 4: CODIFICACIÓN Y COMPRESIÓN ---
* `cumpleShannon(probabilidades, codigos, N=1)` -> bool
* `algoritmoHuffman(probabilidades)` -> list (Códigos)
* `algoritmoShannonFano(probabilidades)` -> list (Códigos)
* `recursividadShannonFano(items, codigos, prefijo='')` -> (internal recursive)
* `calculoRendimiento(codigos, probabilidades)` -> float
* `calculoRedundancia(codigos, probabilidades)` -> float
* `decodificarMensaje(alfabeto, codigos, cadena)` -> str
* `codificarABytes(alfabeto, codigos, mensaje)` -> bytearray
* `decodificarDeBytes(alfabeto, codigos, bytes)` -> str
* `calcularTasaCompresion(msj_og, msj_bytes)` -> Fraction
* `comprimirRLC(mensaje)` -> bytearray
* `calcularHamming(codigos)` -> int
* `calcularErroresDetectables(codigos)` -> int
* `calcularErroresCorregibles(codigos)` -> int
* `agregarBitParidad(caracter)` -> int
* `verificarParidad(byte_recibido)` -> bool
* `genBytearrayMatrizParidad(mensaje)` -> bytearray (Matriz 2D)
* `decodificarParidadMatriz(bytes)` -> str (Corrige errores)

## --- TP 5: CANALES (Probabilidades y Entropías) ---
* `genMatrizCanal(entrada, salida)` -> list[list]
* `calcularProbabilidadesSalida(probs_priori, matriz_canal)` -> list (P(B))
* `calcularMatrizPosteriori(probs_priori, matriz_canal)` -> list[list] (P(A|B))
* `calcularMatrizSimultanea(probs_priori, matriz_canal)` -> list[list] (P(A,B))
* `calcularEntropiasPosteriori(probs_priori, matriz_canal)` -> list (H(A|Bj))
* `calcularEquivocacion(probs_priori, matriz_canal)` -> float (H(A|B))
* `calcularPerdida(probs_priori, matriz_canal)` -> float (H(B|A))
* `calcularEntropiaAfin(probs_priori, matriz_canal)` -> float (H(A,B))
* `calcularInformacionMutua(probs_priori, matriz_canal)` -> float (I(A;B))

## --- TP 6: CANALES (Capacidad y Reducción) ---
* `esCanalSinRuido(matriz)` -> bool
* `esCanalDeterminante(matriz)` -> bool
* `esCanalUniforme(matriz)` -> bool
* `calcularMatrizCompuesta(matriz_AB, matriz_BC)` -> list[list] (P(C|A))
* `verificarColumnasProporcionales(matriz, c1, c2)` -> bool
* `proporcionalEnUnSentido(matriz, a, b, tol=1e-9)` -> bool
* `genMatrizReduccion(matriz, c1, c2)` -> list[list] (Transformación)
* `realizarReduccionMaxima(matriz)` -> list[list]
* `calcularCapacidadEspecial(matriz)` -> float (Para det/sin ruido/unif)
* `estimarCapacidadCanalBinario(matriz, paso)` -> (float, float)
* `calcularProbabilidadError(probs_priori, matriz)` -> float (Según Guía TP)

## --- UTILS (Impresión) ---
* `genProbabilidadesEquiprobables(cant)` -> list
* `imprimirVector(vector, decimales=4)`
* `imprimirMatriz(matriz, decimales=4)`
* `imprimirEntropiasPosteriori(lista, decimales=4)`
* `imprimirBytearray(byte_array)`