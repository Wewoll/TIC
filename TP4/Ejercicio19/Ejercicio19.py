import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

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