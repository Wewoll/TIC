import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import TP6_Funciones
import utils

# Estima la capacidad de un canal binario
def estimarCapacidadCanalBinario(matriz_canal, paso):
    """
    Ejercicio 10:
    Estima la capacidad de un canal binario probando diferentes
    probabilidades a priori P(A) con un 'paso' determinado.
    
    Retorna (Capacidad_estimada, p_optima)
    """
    
    # Inicializamos los valores máximos
    capacidad_estimada = -1.0
    probabilidad_optima = 0.0
    
    # --- Bucle de "Fuerza Bruta" ---
    # Convertimos 1/paso a un entero para un bucle seguro
    # (Ej: si paso=0.1, num_pasos = 10. El bucle irá de 0 a 10)
    num_pasos = int(1.0 / paso)
    
    # Usamos num_pasos + 1 para asegurar que el bucle incluya el 1.0
    for i in range(num_pasos + 1):
        
        # 1. Calculamos la probabilidad 'p' actual
        p = i * paso
        
        # 2. Creamos el vector de probabilidad a priori
        probs_a_priori = [p, 1 - p]
        
        # 3. Calculamos la Información Mutua para este 'p'
        #    (Usamos la función que ya creamos en el TP5)
        info_mutua_actual = utils.calcularInformacionMutua(probs_a_priori, matriz_canal)
        
        # 4. Comparamos y guardamos el máximo
        if info_mutua_actual > capacidad_estimada:
            capacidad_estimada = info_mutua_actual
            probabilidad_optima = p
            
    return (capacidad_estimada, probabilidad_optima)