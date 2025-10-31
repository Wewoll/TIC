import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

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
            
    return TP4_Funciones.decodificarMensaje(alfabeto_fuente, codigos, bits_string)