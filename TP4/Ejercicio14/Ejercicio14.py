import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

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
    
    # return "".join(mensaje_decodificado) si quiero todo junto
    return " ".join(mensaje_decodificado)

# Del ejercicio 2
fuente = ["S1", "S2", "S3", "S4"]
probs = [0.3 , 0.1, 0.4, 0.2]
codigos = ["BA", "CAB", "A", "CBA"]

cadena_a = "ABACBAACABABAACBABA"
cadena_b = "BACBAAABAAACBABACAB"
cadena_c = "CBAABACBABAAACABABA"

cadenas = [cadena_a, cadena_b, cadena_c]
i = 96

for cadena in cadenas:
    i += 1
    mensaje = decodificarMensaje(fuente, codigos, cadena)
    print(f"{chr(i)}. {mensaje}")