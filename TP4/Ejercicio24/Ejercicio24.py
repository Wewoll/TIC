import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

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