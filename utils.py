import math
import random
import itertools
from fractions import Fraction

"""""""""""""""""""""""""""""""""""""""""""""
---------========   T P 2   ========---------
"""""""""""""""""""""""""""""""""""""""""""""

# Calculo de la Informacion de la probabilidad 'p' en base 'base' (2 por defecto)
def calculoInformacion(p, base = 2):
    if p <= 0:
        return 0
    return math.log(1/p, base)


# Calculo de la Entropia de una fuente de informacion nula
def calculoEntropia(probabilidades, base = 2):
    informacion = [calculoInformacion(p, base) for p in probabilidades]
    return sum(a * b for a, b in zip(probabilidades, informacion))


# Generar el alfabeto de una cadena
def genAlfabeto(cadena):
    alfabeto = []
    for simbolo in cadena:
        if simbolo not in alfabeto:
            alfabeto.append(simbolo)
    alfabeto.sort()
    return alfabeto


# Generar las probabilidades de un alfabeto de una cadena
def genProbabilidadesAlf(cadena):
    alfabeto = genAlfabeto(cadena)
    probabilidades = []
    cant_simboloacteres = len(cadena)
    for simbolo in alfabeto:
        probabilidades.append(cadena.count(simbolo) / cant_simboloacteres)

    return probabilidades


# Generar mensaje de la fuente de memoria nula
def genMensaje(alfabeto, probabilidades, longitud_msj = 20):
    # crear distribución acumulada
    prob_acum = []
    total = 0
    for p in probabilidades:
        total += p
        prob_acum.append(total)

    msj = []
    for _ in range(longitud_msj):
        r = random.random()  # número aleatorio entre 0 y 1
        for simbolo, limite in zip(alfabeto, prob_acum):
            if r < limite:
                msj.append(simbolo)
                break

    return "".join(msj)


# Calculo de la Entropia en fuente binaria (W)
def calculoEntropiaBin(probW, base = 2):
    probabilidades = [probW, 1 - probW]
    return calculoEntropia(probabilidades, base)


# Generar alfabeto de extension de orden N
def genAlfabetoOrdN(alfabeto, N):
    if N == 1:
        return alfabeto
    else:
        alf_menor = genAlfabetoOrdN(alfabeto, N - 1)
        alf_extension = []
        for prefijo in alf_menor:
            for simbolo in alfabeto:
                alf_extension.append(prefijo + simbolo)

    return alf_extension


# Generar probabilidades del alfabeto de extencion de orden N
def genProbabilidadesAlfOrdN(probabilidades, N):
    if N == 1:
        return probabilidades
    else:
        prob_menor = genProbabilidadesAlfOrdN(probabilidades, N - 1)
        prob_extension = []
        for prob_parcial in prob_menor:
            for p in probabilidades:
                prob_extension.append(prob_parcial * p)

    return prob_extension


# itertools: Generar alfabeto y probabilidades de orden N
def itertools_GenListasOrdN(alfabeto, probabilidades, N):
    # Generar alfabeto extendido
    alf_extension = ["".join(tupla) for tupla in itertools.product(alfabeto, repeat = N)]
    
    # Generar probabilidades extendidas
    prob_extension = []
    for tupla in itertools.product(range(len(alfabeto)), repeat = N):
        p = 1
        for i in tupla:
            p *= probabilidades[i]
        prob_extension.append(p)

    return alf_extension, prob_extension


# Generar vector estacionario
def genVectorEstacionario(matriz, tolerancia = 0.01, iteraciones = 500):
    N = len(matriz)
    dif_max = 1
    vector_estacionario = [1/N for _ in range(N)]  # Inicializar vector estacionario equiprobable

    # Ciclo para generar un vector estacionario
    while (0 < iteraciones and dif_max > tolerancia):
        iteraciones -= 1
        vector_est_ant = vector_estacionario.copy()
        vector_estacionario = [0 for _ in range(N)]

        for i in range(N):
            for j in range(N):
                vector_estacionario[i] += matriz[i][j] * vector_est_ant[j]
            
        dif_max = maxDifVec(vector_est_ant, vector_estacionario)

    return vector_estacionario


# Busca la maxima diferencia entre dos valores paralelos
def maxDifVec(vector_ant, vector_nuevo):
    dif_max = 0
    for i in range(len(vector_ant)):
        dif = abs(vector_ant[i] - vector_nuevo[i])
        if dif > dif_max:
            dif_max = dif
    return dif_max


# Calculo de la Entropia de una fuente de Markov
def calculoEntropiaMarkov(matriz, base = 2):
    entropiaMarkov = 0
    vector_estacionario = genVectorEstacionario(matriz)
    N = len(matriz)

    for j in range(N):
        # Tomo la columna j (todas las probabilidades de ir a otro estado desde j)
        prob_columna = [matriz[i][j] for i in range(N)]

        # Entropía condicional desde el estado j
        H_cond = calculoEntropia(prob_columna, base)

        # Pondero por la probabilidad de estar en el estado j
        entropiaMarkov += vector_estacionario[j] * H_cond

    return entropiaMarkov


# Generar matriz de ocurrencias
def genMatrizOcurrencias(cadena):
    alfabeto = genAlfabeto(cadena)
    N = len(alfabeto)
    matriz_ocurrencias = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(len(cadena) - 1):
        origen = alfabeto.index(cadena[i])
        destino = alfabeto.index(cadena[i + 1])
        matriz_ocurrencias[destino][origen] += 1

    return matriz_ocurrencias


# Generar matriz de probabilidades (de transicion, normalizando la de ocurrencias)
def genMatrizProbabilidades(matriz_ocurrencias):
    N = len(matriz_ocurrencias)
    matriz_prob = [[0 for _ in range(N)] for _ in range(N)]

    for j in range(N):  # columna
        col_sum = sum(matriz_ocurrencias[i][j] for i in range(N))
        if col_sum > 0:
            for i in range(N):  # fila
                matriz_prob[i][j] = matriz_ocurrencias[i][j] / col_sum

    return matriz_prob


# Generar matriz de transicion
def genMatrizTransicion(cadena):
    matriz = genMatrizOcurrencias(cadena)
    matriz = genMatrizProbabilidades(matriz)
    return matriz


# Generar mensaje de la fuente Markov
def genMensajeMarkov(alfabeto, matriz, longitud_msj = 20, estado_inicial = None):
    N = len(alfabeto)

    # Si no se pasa estado inicial, arrancamos al azar
    if estado_inicial is None:
        estado_actual = random.randrange(N)
    else:
        estado_actual = alfabeto.index(estado_inicial)

    msj = [alfabeto[estado_actual]]

    for _ in range(longitud_msj - 1):
        # Probabilidades de transición desde este estado (columna)
        probs = [matriz[i][estado_actual] for i in range(N)]

        # Elegir siguiente estado según probs
        siguiente_estado = random.choices(range(N), weights = probs, k = 1)[0]

        msj.append(alfabeto[siguiente_estado])
        estado_actual = siguiente_estado

    return "".join(msj)


# Analizar si una fuente de memoria es nula o no nula
def esFuenteSinMemoria(matriz, tolerancia):
    """
    Devuelve True si la fuente representada por la matriz de transición
    puede considerarse sin memoria, es decir, si las filas son casi iguales
    dentro de la tolerancia dada.
    """
    
    N = len(matriz)
    dif_max = 0
    
    for i in range(N):
        dif_fila = max(matriz[i]) - min(matriz[i])
        
        if dif_fila > dif_max:
            dif_max = dif_fila

    return dif_max < tolerancia


# Analizar si la matriz es ergodica o no
def esFuenteErgodica(matriz, tol = 1e-6):
    """
    Determina si una fuente de Markov es ergódica.
    La matriz debe tener columnas que sumen 1.
    
    Retorna True si es ergódica, False en caso contrario.
    """
    N = len(matriz)
    
    # Generar matriz de conectividad: 1 si hay transición posible, 0 si no
    alcanzable = [[1 if matriz[i][j] > tol else 0 for j in range(N)] for i in range(N)]
    
    # Propagamos conexiones hasta N-1 pasos
    for _ in range(N - 1):
        nueva_conectividad = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                # j es alcanzable desde i si existe k tal que i->k y k->j
                for k in range(N):
                    if alcanzable[i][k] and alcanzable[k][j]:
                        nueva_conectividad[i][j] = 1
                        break  # suficiente con un camino
        alcanzable = nueva_conectividad
    
    # Si hay algún par de estados que no se alcanza, no es ergódica
    for i in range(N):
        for j in range(N):
            if alcanzable[i][j] == 0:
                return False
    return True


"""""""""""""""""""""""""""""""""""""""""""""
---------========   T P 3   ========---------
"""""""""""""""""""""""""""""""""""""""""""""

# Verifica si una lista de codigos es 'No Singular'
def esNoSingular(codigos):
    return len(codigos) == len(set(codigos))


# Verifica si una lista de codigos es 'No Singular', mediante un for
def esNoSingularFor(codigos):
    n = len(codigos)
    for i in range(n):
        for j in range(i+1, n):
            if codigos[i] == codigos[j]:
                return False  # encontró dos iguales → no es no singular
    return True  # todas distintas


# Verifica si una lista de codigos es 'Instantaneo'
def esInstantaneo(codigos):
    n = len(codigos)
    for i in range(n):
        for j in range(n):
            if i != j:
                if codigos[j].startswith(codigos[i]):
                    return False  # cod[i] es prefijo de cod[j]
    return True


# Verifica si una lista de codigos es 'Univoco'
def esUnivoco(codigos):
    i = -1
    C = set(codigos)
    S1 = set(codigos)
    set_vistos = []
    set_vistos.append(S1)

    # Iterar para construir S2, S3, ...
    while True:
        s_sig = set()
        i += 1

        for x in S1:
            for y in set_vistos[i]:
                if x != y:
                    # Si x es prefijo de y, agregar sufijo de y
                    if y.startswith(x):
                        s_sig.add(y[len(x):])

                    # Si y es prefijo de x, agregar sufijo de x
                    if x.startswith(y):
                        s_sig.add(x[len(y):])

        # Condición 1: ¿algún elemento de Si está en C?
        if any(pal in C for pal in s_sig):
            return False  # no es unívoco

        # Condición 2: ¿ya vimos este conjunto antes?
        if s_sig in set_vistos:
            return True  # es unívoco
        
        set_vistos.append(s_sig)


# Devolver que tipo de codigo
def tipoCodigo(codigos):
    if esNoSingular(codigos):
        if esInstantaneo(codigos):
            return "Instantáneo"
        else:
            if esUnivoco(codigos):
                return "Unívoco"
            else:        
                return "No singular"
    else:
        return "Bloque"


# Generar alfabeto de los codigos
def genAlfabetoCodigos(codigos):
    cadena = ""

    for cod in codigos:
        for caracter in cod:
            if caracter not in cadena:
                cadena += caracter

    return cadena


# Generar longitudes de los codigos
def genLongitudesCodigos(codigos):
    return [len(palabra) for palabra in codigos]


# Calculo de la sumatoria de la inecuacion de Kraft
def calculoInecuacionKraft(codigos):
    r = len(genAlfabetoCodigos(codigos))
    longitudes = genLongitudesCodigos(codigos)
    return sum(r ** (-l) for l in longitudes)


# Calculo de la Informacion de la probabilidad 'p' en base 'r'
def calculoInformacionR(p, r):
    if p <= 0:
        return 0
    return math.log(1/p, r)


# Calculo de la entropia en base 'r'
def calculoEntropiaCP(codigos, probabilidades):
    r = len(genAlfabetoCodigos(codigos))
    informacion = [calculoInformacionR(p, r) for p in probabilidades]
    return sum(a * b for a, b in zip(probabilidades, informacion))


# Calculo de la longitud media
def calculoLongitudMedia(codigos, probabilidades):
    longitudes = genLongitudesCodigos(codigos)
    return sum(a * b for a, b in zip(probabilidades, longitudes))


# Calculo de la longitud ideal
def calculoLongitudIdeal(probabilidades, r):
    return [math.ceil(calculoInformacionR(p, r)) for p in probabilidades]


# Verificar si es codigo compacto
def esCodigoCompacto(codigos, probabilidades):
    if not (esNoSingular(codigos) and esInstantaneo(codigos)):
        return False
    
    r = len(genAlfabetoCodigos(codigos))
    longitudes = genLongitudesCodigos(codigos)
    long_ideales = calculoLongitudIdeal(probabilidades, r)

    for li, l in zip(long_ideales, longitudes):
        if l > li:
            return False
            
    return True


# Generar mensaje de la fuente de memoria
def genMensajeCP(codigos, probabilidades, N):
    msj = [random.choices(codigos, weights=probabilidades)[0] for _ in range(N)]
    return ''.join(msj)


"""""""""""""""""""""""""""""""""""""""""""""
---------========   T P 4   ========---------
"""""""""""""""""""""""""""""""""""""""""""""

# Verifica si se cumple el Primer Teorema de Shannon (pasar codigos extendidos)
def cumpleShannon(probabilidades, codigos, N = 1):
    prob_ext = genProbabilidadesAlfOrdN(probabilidades, N)
    long_media = calculoLongitudMedia(codigos, prob_ext)
    entropia = calculoEntropiaCP(codigos, probabilidades)

    long_media_norm = long_media / N
    lim_inf = entropia
    lim_sup = entropia + (1 / N)

    return  lim_inf <= long_media_norm < lim_sup


# Algoritmo de Huffman (iterativo)
def algoritmoHuffman(probabilidades):
    items = [[prob, [idx]] for idx, prob in enumerate(probabilidades)]
    codigos = [''] * len(probabilidades)

    while len(items) > 1:
        items.sort(key=lambda x: x[0])
        prob_baja, simbolos_bajos = items.pop(0)
        prob_alta, simbolos_altos = items.pop(0)

        for idx in simbolos_bajos:
            codigos[idx] = '0' + codigos[idx]

        for idx in simbolos_altos:
            codigos[idx] = '1' + codigos[idx]

        nuevo_item = [prob_baja + prob_alta, simbolos_bajos + simbolos_altos]
        items.append(nuevo_item)

    return codigos


# Algoritmo de Shannon-Fano, inicializacion
def algoritmoShannonFano(probabilidades):
    items = [[prob, idx] for idx, prob in enumerate(probabilidades)]
    items.sort(key=lambda x: x[0], reverse = True)
    codigos = [''] * len(probabilidades)
    recursividadShannonFano(items, codigos)
    return codigos

# Algoritmo de Shannon-Fano, parte recursiva
def recursividadShannonFano(items, codigos, prefijo = ''):
    N = len(items)
    if N == 1:
        codigos[items[0][1]] = prefijo
    else:   
        suma_total = sum(nodo[0] for nodo in items)
        suma_mitad = suma_total / 2

        suma_parcial = 0
        punto_corte = 0
        min_diferencia = float('inf')

        for i in range(len(items) - 1):
            suma_parcial += items[i][0]
            diferencia = abs(suma_parcial - suma_mitad)
            if diferencia < min_diferencia:
                min_diferencia = diferencia
                punto_corte = i + 1

        grupo_superior = items[:punto_corte]
        grupo_inferior = items[punto_corte:]
        
        recursividadShannonFano(grupo_superior, codigos, prefijo + '1')
        recursividadShannonFano(grupo_inferior, codigos, prefijo + '0')


# Calculo del Rendimiento (η)
def calculoRendimiento(codigos, probabilidades):
    entropia = calculoEntropiaCP(codigos, probabilidades)
    long_media = calculoLongitudMedia(codigos, probabilidades)

    return entropia / long_media


# Calculo de la Redundancia (1 - η)
def calculoRedundancia(codigos, probabilidades):
    return 1 - calculoRendimiento(codigos, probabilidades)


# Decodificar el mensaje de una cadena
def decodificarMensaje(alfabeto_fuente, codigos, cadena_codificada):
    mapa_decodificacion = dict(zip(codigos, alfabeto_fuente))

    mensaje_decodificado = []
    buffer_actual = ""
    
    for caracter in cadena_codificada:
        buffer_actual += caracter
        
        if buffer_actual in mapa_decodificacion:
            simbolo = mapa_decodificacion[buffer_actual]
            mensaje_decodificado.append(simbolo)
            buffer_actual = ""

    if buffer_actual:
        return f"ERROR: No se pudo decodificar. Sobrante en el buffer: '{buffer_actual}'"
    
    # return " ".join(mensaje_decodificado) si quiero todo separado
    return "".join(mensaje_decodificado)


# Codifica un mensaje fuente en una secuencia de bytes
def codificarABytes(alfabeto_fuente, codigos, mensaje):
    mapa_codificacion = dict(zip(alfabeto_fuente, codigos))
    bits_string = "".join([mapa_codificacion[simbolo] for simbolo in mensaje])
    
    padding = (8 - len(bits_string) % 8) % 8
    bits_string += '0' * padding
    
    # El primer byte del resultado guardará cuántos bits de relleno se usaron.
    # Esto es crucial para que el decodificador sepa cuántos bits ignorar al final.
    resultado_bytes = bytearray([padding])
    
    # Recorrer la cadena de bits en trozos de 8 (bytes).
    for i in range(0, len(bits_string), 8):
        trozo_de_8_bits = bits_string[i:i+8]
        # Convertir el trozo de "10101100" a un número entero (byte).
        valor_byte = int(trozo_de_8_bits, 2)
        resultado_bytes.append(valor_byte)
        
    return resultado_bytes


# Decodifica una secuencia de bytes para retornar el mensaje original.
def decodificarDeBytes(alfabeto_fuente, codigos, secuencia_bytes):
    # Leer la "nota": el primer byte nos dice cuántos bits de relleno hay.
    padding = secuencia_bytes[0]
    
    bits_string = ""
    for valor_byte in secuencia_bytes[1:]:
        # Convertimos el número (ej: 179) a su representación binaria (ej: '0b10110011')
        # y le quitamos el prefijo '0b'.
        bits_del_byte = bin(valor_byte)[2:]
        # Nos aseguramos de que cada trozo tenga 8 bits, rellenando con ceros a la izquierda.
        bits_del_byte = bits_del_byte.zfill(8)
        bits_string += bits_del_byte
        
    # Quitar los bits de relleno que se agregaron al codificar.
    if padding > 0:
        bits_string = bits_string[:-padding]
            
    return decodificarMensaje(alfabeto_fuente, codigos, bits_string)


# Calcula la tasa de compresion
def calcularTasaCompresion(msj_og, msj_bytes):
    tamano_original = len(msj_og)
    tamano_comprimido = len(msj_bytes)
    tasa_compresion = 0
    
    if tamano_comprimido != 0:
        tasa_compresion = Fraction(tamano_original, tamano_comprimido)
        # tasa_compresion = tamano_original / tamano_comprimido

    return tasa_compresion


# Comprime un mensaje usando Run Length Coding (RLC) y devuelve un bytearray.
def comprimirRLC(mensaje):        
    resultado_bytes = bytearray()
    i = 0
    n = len(mensaje)
    
    while i < n:
        caracter_actual = mensaje[i]
        contador = 0
        
        while i < n and mensaje[i] == caracter_actual and contador < 255:
            contador += 1
            i += 1
            
        valor_ascii = ord(caracter_actual)
        resultado_bytes.append(valor_ascii)
        resultado_bytes.append(contador)
        
    return resultado_bytes


# Calcular la distancia de Hamming (distancia mínima entre cualquier par de sus palabras código)
def calcularHamming(codigos):
    n = len(codigos)        
    min_distancia = float('inf')
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = sum(1 for c1, c2 in zip(codigos[i], codigos[j]) if c1 != c2)
            
            if dist < min_distancia:
                min_distancia = dist
                
    return min_distancia


# Calcula la cantidad de errores que un codigo puede detectar (Hamming - 1)
def calcularErroresDetectables(codigos):
    return calcularHamming(codigos) - 1


# Calcula la cantidad de errores que un codigo puede corregir ((Hamming - 1) / 2)
def calcularErroresCorregibles(codigos):
    return (calcularHamming(codigos) - 1) // 2


# Crea un byte con el bit de paridad (par) de un caracter ASCII
def agregarBitParidad(caracter):
    valor_ascii_7bits = ord(caracter) & 0x7F
    cantidad_de_unos = bin(valor_ascii_7bits).count('1')
    bit_paridad = cantidad_de_unos % 2
    byte_desplazado = valor_ascii_7bits << 1
    byte_final = byte_desplazado | bit_paridad
    
    return byte_final


# Recibe un byte con paridad y verifica si es correcto
def verificarParidad(byte_recibido):    
    bit_paridad_recibido = byte_recibido & 1
    datos_7bits = byte_recibido >> 1
    cantidad_de_unos = bin(datos_7bits).count('1')
    bit_paridad_calculado = cantidad_de_unos % 2
    
    return bit_paridad_recibido == bit_paridad_calculado


# Genera un bytearray que contiene el mensaje con bits de paridad longitudinal, vertical y cruzada.
def genBytearrayMatrizParidad(mensaje):
    N = len(mensaje)
    matriz_bits = [[0] * 8 for _ in range(N + 1)]
    
    for i, caracter in enumerate(mensaje):
        valor_ascii_7bits = ord(caracter) & 0x7F
        bits_string = bin(valor_ascii_7bits)[2:].zfill(7)
        
        cantidad_de_unos = 0
        for j, bit in enumerate(bits_string):
            if bit == '1':
                matriz_bits[i + 1][j] = 1
                cantidad_de_unos += 1
        
        matriz_bits[i + 1][7] = cantidad_de_unos % 2
        

    for j in range(8):
        cantidad_de_unos = 0
        for i in range(1, N + 1):
            cantidad_de_unos += matriz_bits[i][j]
            
        matriz_bits[0][j] = cantidad_de_unos % 2
    
    resultado_bytes = bytearray()
    for i in range(N + 1):
        bits_fila = "".join(str(bit) for bit in matriz_bits[i])
        valor_byte = int(bits_fila, 2)
        resultado_bytes.append(valor_byte)
        
    return resultado_bytes


# Decodifica una secuencia de bytes (bytearray) con paridad
# Corrige un error simple y devuelve el mensaje ASCII recuperado o cadena vacía si no se puede corregir.
def decodificarParidadMatriz(secuencia_bytes):
    mensaje_recuperado = ""
    error_detectado = False
    error_incorregible = False

    # --- 1. Matriz de bits ---
    N_filas_total = len(secuencia_bytes)          # incluye fila 0 de paridad
    matriz = []
    for byte in secuencia_bytes:
        bits = bin(byte)[2:].zfill(8)
        matriz.append([int(b) for b in bits])

    # --- 2. Comprobación de paridades ---
    fila_fallida = -1
    col_fallida = -1
    errores_fila = 0
    errores_col = 0

    # Paridad horizontal (filas de datos)
    for i in range(1, N_filas_total):             # filas 1..N_filas_datos
        if sum(matriz[i]) % 2 != 0:
            fila_fallida = i
            errores_fila += 1

    # Paridad vertical (columnas, incluyendo fila 0)
    for j in range(8):
        if sum(matriz[i][j] for i in range(N_filas_total)) % 2 != 0:
            col_fallida = j
            errores_col += 1

    # Paridad cruzada: comprobamos paridad total de toda la matriz
    total_unos = sum(sum(fila) for fila in matriz)
    cruzado_ok = (total_unos % 2) == 0

    # --- 3. Análisis de errores ---
    if errores_fila == 0 and errores_col == 0 and cruzado_ok:
        # sin errores
        pass
    elif errores_fila == 1 and errores_col == 1 and not cruzado_ok:
        # error simple -> corregible
        original = matriz[fila_fallida][col_fallida]
        matriz[fila_fallida][col_fallida] = 1 - original
        error_detectado = True
    else:
        # múltiples errores o inconsistencia
        error_incorregible = True

    # --- 4. Reconstrucción ---
    if not error_incorregible:
        chars = []
        for i in range(1, N_filas_total):
            bits_datos = matriz[i][:7]
            ascii_val = int("".join(str(b) for b in bits_datos), 2)
            chars.append(chr(ascii_val))
        mensaje_recuperado = "".join(chars)
    else:
        mensaje_recuperado = ""

    # --- 5. Estado final (prints informativos) ---
    if error_incorregible:
        print("[Error] Múltiples errores detectados o inconsistencia en paridad cruzada.")
    elif error_detectado:
        print(f"[Corrección] Error simple corregido en fila {fila_fallida}, columna {col_fallida}.")
    else:
        print("[OK] Sin errores detectados.")

    return mensaje_recuperado


"""""""""""""""""""""""""""""""""""""""""""""
---------========   T P 5   ========---------
"""""""""""""""""""""""""""""""""""""""""""""

# Genera la matriz que representa al canal de las cadenas recibidas
def genMatrizCanal(secuencia_entrada, secuencia_salida):
    alfabeto_A = genAlfabeto(secuencia_entrada)
    alfabeto_B = genAlfabeto(secuencia_salida)
    
    conteo_A = {simbolo: 0 for simbolo in alfabeto_A}
    conteo_pares = {sim_A: {sim_B: 0 for sim_B in alfabeto_B} for sim_A in alfabeto_A}
        
    for i in range(len(secuencia_entrada)):
        sim_A = secuencia_entrada[i]
        sim_B = secuencia_salida[i]
        
        conteo_pares[sim_A][sim_B] += 1
        conteo_A[sim_A] += 1
        
    matriz_canal = []
    for sim_A in alfabeto_A:
        fila = []
        denominador = conteo_A[sim_A]
        
        for sim_B in alfabeto_B:
            if denominador == 0:
                fila.append(0.0)
            else:
                numerador = conteo_pares[sim_A][sim_B]
                prob = numerador / denominador
                fila.append(prob)
                
        matriz_canal.append(fila)
        
    return matriz_canal


# Calcula la lista de probabilidades de los símbolos de salida P(B)
# P(B) = Suma sobre A de P(A, B)
def calcularProbabilidadesSalida(probs_priori_A, matriz_canal_B_dado_A):
    matriz_simultanea = calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A)

    num_A = len(matriz_simultanea)
    num_B = len(matriz_simultanea[0])
    probs_salida_B = [0.0] * num_B
    
    for j in range(num_B):
        for i in range(num_A):
            probs_salida_B[j] += matriz_simultanea[i][j]
        
    return probs_salida_B


# Calcula la matriz de probabilidades a posteriori P(A|B)
# P(A|B) = P(A, B) / P(B)
def calcularMatrizPosteriori(probs_priori_A, matriz_canal_B_dado_A):
    matriz_simultanea = calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A)
    probs_salida_B = calcularProbabilidadesSalida(probs_priori_A, matriz_canal_B_dado_A)

    num_A = len(matriz_simultanea)
    num_B = len(matriz_simultanea[0])
    matriz_posteriori = [[0.0] * num_B for _ in range(num_A)]
    
    for i in range(num_A):
        for j in range(num_B):
            if probs_salida_B[j] == 0:
                matriz_posteriori[i][j] = 0.0
            else:
                matriz_posteriori[i][j] = matriz_simultanea[i][j] / probs_salida_B[j]
    
    return matriz_posteriori


# Calcula la matriz de probabilidades de eventos simultáneos P(A, B)
# P(A, B) = P(B|A) * P(A)
def calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A):
    num_A = len(probs_priori_A)
    num_B = len(matriz_canal_B_dado_A[0])
    matriz_simultanea = [[0.0] * num_B for _ in range(num_A)]
    
    for i in range(num_A):
        for j in range(num_B):
            matriz_simultanea[i][j] = matriz_canal_B_dado_A[i][j] * probs_priori_A[i]
            
    return matriz_simultanea


# Calcula la lista de entropías a posteriori H(A|Bj)
# (Calcula la entropía de cada columna de la matriz P(A|B))
def calcularEntropiasPosteriori(probs_priori_A, matriz_canal_B_dado_A):
    matriz_posteriori = calcularMatrizPosteriori(probs_priori_A, matriz_canal_B_dado_A)
        
    num_A = len(matriz_posteriori)
    num_B = len(matriz_posteriori[0])  
    lista_entropias_posteriori = []
    
    for j in range(num_B):
        columna_j = [matriz_posteriori[i][j] for i in range(num_A)]
        entropia_col = calculoEntropia(columna_j)
        lista_entropias_posteriori.append(entropia_col)
        
    return lista_entropias_posteriori


# Calcula la Equivocación o Ruido H(A|B)
def calcularEquivocacion(probs_priori_A, matriz_canal_B_dado_A):
    entropias_posteriori = calcularEntropiasPosteriori(probs_priori_A, matriz_canal_B_dado_A)
    probs_salida_B = calcularProbabilidadesSalida(probs_priori_A, matriz_canal_B_dado_A)
    equivocacion = sum(p_b * h_post for p_b, h_post in zip(probs_salida_B, entropias_posteriori))
        
    return equivocacion


# Calcula la Pérdida H(B|A)
def calcularPerdida(probs_priori_A, matriz_canal_B_dado_A):
    num_A = len(probs_priori_A)
    perdida = 0.0
    
    for i in range(num_A):
        entropia_fila = calculoEntropia(matriz_canal_B_dado_A[i])
        perdida += probs_priori_A[i] * entropia_fila
        
    return perdida


# Calcula la Entropía Afín o Conjunta H(A, B).
def calcularEntropiaAfin(probs_priori_A, matriz_canal_B_dado_A):
    matriz_simultanea = calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A)

    lista_probs_simultaneas = []
    for fila in matriz_simultanea:
        lista_probs_simultaneas.extend(fila)

    return calculoEntropia(lista_probs_simultaneas)


# Calcula la Información Mutua I(A, B) por su fórmula de definición
def calcularInformacionMutua(probs_priori_A, matriz_canal_B_dado_A):
    probs_A = probs_priori_A
    probs_B = calcularProbabilidadesSalida(probs_priori_A, matriz_canal_B_dado_A)
    matriz_A_B = calcularMatrizSimultanea(probs_priori_A, matriz_canal_B_dado_A)
        
    num_A = len(matriz_A_B)
    num_B = len(matriz_A_B[0]) 
    info_mutua = 0.0
    
    for i in range(num_A):
        for j in range(num_B):
            p_a = probs_A[i]
            p_b = probs_B[j]
            p_ab = matriz_A_B[i][j]
            
            if p_ab > 0:
                termino = p_ab * math.log2(p_ab / (p_a * p_b))
                info_mutua += termino
                
    return info_mutua


"""""""""""""""""""""""""""""""""""""""""""""
---------========   T P 6   ========---------
"""""""""""""""""""""""""""""""""""""""""""""




"""""""""""""""""""""""""""""""""""""""""""""
---------========   Utils   ========---------
"""""""""""""""""""""""""""""""""""""""""""""

# Imprime un vector con formato controlando los decimales
def imprimirVector(vector, decimales = 4):
    elementos_formateados = []
    
    formato = f".{decimales}f"
    
    for item in vector:
        if isinstance(item, (int, float)):
            elementos_formateados.append(f"{item:{formato}}")
        else:
            elementos_formateados.append(str(item))
            
    string_interior = ", ".join(elementos_formateados)
    print(f"[{string_interior}]")


# Imprime una matriz con formato controlando los decimales
def imprimirMatriz(matriz, decimales = 4):
    print("[")
    for fila in matriz:
        print("  ", end="")
        imprimirVector(fila, decimales=decimales)
    print("]")


# Imprime una lista de entropías a posteriori con etiquetas genéricas
def imprimirEntropiasPosteriori(lista_entropias, decimales = 4):
    formato = f".{decimales}f"
    
    for j, entropia in enumerate(lista_entropias, start=1):
        etiqueta = f"b{j}"
        print(f"  H(A|{etiqueta}): {entropia:{formato}} bits")


# Genera una lista de probabilidades equiprobables.
def genProbabilidadesEquiprobables(cant):
    prob = 1.0 / cant
    return [prob] * cant


# Bloques de Texto para copiar y pegar
asd = 0
if asd == 1:
    probs_priori = []
    matriz_canal = [[]]
    decimales = 4

    print("Probabilidades a Priori P(A):")
    imprimirVector(probs_priori, decimales)

    print("Matriz del Canal P(B|A):")
    imprimirMatriz(matriz_canal, decimales)

    probs_salida = calcularProbabilidadesSalida(probs_priori, matriz_canal)
    print("Probabilidades de Salida P(B):")
    imprimirVector(probs_salida, decimales)

    matriz_simultanea = calcularMatrizSimultanea(probs_priori, matriz_canal)
    print("Matriz de Eventos Simultaneos P(A, B):")
    imprimirMatriz(matriz_simultanea, decimales)

    matriz_posteriori = calcularMatrizPosteriori(probs_priori, matriz_canal)
    print("Matriz a Posteriori P(A|B):")
    imprimirMatriz(matriz_posteriori, decimales)

    entropias_posteriori = calcularEntropiasPosteriori(probs_priori, matriz_canal)
    print("Entropias a Posteriori H(A|Bj):")
    imprimirEntropiasPosteriori(entropias_posteriori, decimales)

    entropia_priori = calculoEntropia(probs_priori)
    print(f"Entropia a Priori H(A): {entropia_priori:.{decimales}f} bits")

    entropia_salida = calculoEntropia(probs_salida)
    print(f"Entropia de Salida H(B): {entropia_salida:.{decimales}f} bits")

    equivocacion = calcularEquivocacion(probs_priori, matriz_canal)
    print(f"Equivocacion H(A|B): {equivocacion:.{decimales}f} bits")

    perdida = calcularPerdida(probs_priori, matriz_canal)
    print(f"Perdida H(B|A): {perdida:.{decimales}f} bits")

    entropia_afin = calcularEntropiaAfin(probs_priori, matriz_canal)
    print(f"Entropia Afin H(A, B): {entropia_afin:.{decimales}f} bits")

    informacion_mutua = calcularInformacionMutua(probs_priori, matriz_canal)
    print(f"Informacion Mutua I(A, B): {informacion_mutua:.{decimales}f} bits")