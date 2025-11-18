import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP4_Funciones
import utils

# Decodifica un mensaje a partir de su alfabeto, códigos y la cadena codificada
def decodificarMensaje(alfabeto_fuente, codigos, cadena_codificada):
    """
    Toma una cadena de bits (o caracteres codificados) y la traduce
    de vuelta a los símbolos originales usando un diccionario inverso.
    """
    
    # 1. Crear el "Diccionario Inverso" (Mapa de Decodificación)
    #    zip junta las listas: [('0', 'A'), ('10', 'B')...]
    #    dict lo convierte en: {'0': 'A', '10': 'B'...}
    #    Esto permite buscar por CÓDIGO para obtener el SÍMBOLO.
    mapa_decodificacion = dict(zip(codigos, alfabeto_fuente))

    mensaje_decodificado = []
    buffer_actual = ""
    
    # 2. Recorrer la cadena codificada caracter por caracter (bit a bit)
    for caracter in cadena_codificada:
        # Acumulamos el bit leído en el buffer temporal
        buffer_actual += caracter
        
        # 3. Verificar si lo que tenemos en el buffer es un código válido
        #    Gracias a que el código es instantáneo (sin prefijos),
        #    apenas encontramos una coincidencia, sabemos que es única.
        if buffer_actual in mapa_decodificacion:
            
            # Traducimos: Buscamos el símbolo correspondiente al código
            simbolo = mapa_decodificacion[buffer_actual]
            mensaje_decodificado.append(simbolo)
            
            # ¡Importante! Limpiamos el buffer para empezar a leer el siguiente código
            buffer_actual = ""

    # 4. Validación Final
    #    Si al terminar el bucle el buffer NO está vacío, significa que sobraron
    #    bits que no forman un código válido (el mensaje estaba cortado o corrupto).
    if buffer_actual:
        return f"ERROR: No se pudo decodificar. Sobrante en el buffer: '{buffer_actual}'"
    
    # 5. Retornar el resultado
    #    Unimos la lista de símbolos en un solo string.
    #    Usá " " si querés espacios entre símbolos, o "" si querés el mensaje pegado.
    return "".join(mensaje_decodificado)

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