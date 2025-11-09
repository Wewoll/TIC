import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import utils
from fractions import Fraction

# Verifica si se cumple el Primer Teorema de Shannon (pasar codigos extendidos)
def cumpleShannon(probabilidades, codigos, N = 1):
    prob_ext = utils.genProbabilidadesAlfOrdN(probabilidades, N)
    long_media = utils.calculoLongitudMedia(codigos, prob_ext)
    entropia = utils.calculoEntropiaCP(codigos, probabilidades)

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


# Calculo del Rendimiento (η) y la Redundancia (1 - η)
def calculoRendimientoYRedundancia(codigos, probabilidades):
    entropia = utils.calculoEntropiaCP(codigos, probabilidades)
    long_media = utils.calculoLongitudMedia(codigos, probabilidades)

    rendimiento = entropia / long_media
    redundancia = 1 - rendimiento

    return rendimiento, redundancia


# Decodifica un mensaje a partir de su alfabeto, códigos y la cadena codificada
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


# Calcula distancia de Hamming, errores detectables y errores corregibles
def analizarCodigoHamming(codigos):    
    n = len(codigos)
    min_distancia = float('inf')
    
    for i in range(n):
        for j in range(i + 1, n):
            dist = sum(1 for c1, c2 in zip(codigos[i], codigos[j]) if c1 != c2)
            
            if dist < min_distancia:
                min_distancia = dist
                
    errores_detectables = min_distancia - 1
    errores_corregibles = (min_distancia - 1) // 2
    
    return min_distancia, errores_detectables, errores_corregibles


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