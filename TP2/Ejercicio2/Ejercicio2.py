import random

# 2a: generar alfabeto y probabilidades
def genListas(cadena):
    listaA = []
    listaP = []
    for letter in cadena:
        if letter in listaA:
            listaP[listaA.index(letter)] += 1
        else:
            listaA.append(letter)
            listaP.append(1)

    total = sum(listaP)
    listaP = [f / total for f in listaP]  # pasar a probabilidades
    return listaA, listaP

# 2b: generar mensaje de la fuente de memoria nula
def generar_mensaje(alfabeto, probabilidades, longitud):
    # crear distribución acumulada
    acumuladas = []
    total = 0
    for p in probabilidades:
        total += p
        acumuladas.append(total)

    mensaje = []
    for _ in range(longitud):
        r = random.random()  # número aleatorio entre 0 y 1
        for simbolo, limite in zip(alfabeto, acumuladas):
            if r < limite:
                mensaje.append(simbolo)
                break
    return "".join(mensaje)


# --- Ejemplo de uso ---
cadena_original = "Cadena de prueba para el ejercicio de la asignatura"

# 2a
alfabeto, probabilidades = genListas(cadena_original)
print("Alfabeto:", alfabeto)
print("Probabilidades:", probabilidades)

# 2b
nuevo_mensaje = generar_mensaje(alfabeto, probabilidades, 50)  # generar 50 símbolos
print("Mensaje simulado:", nuevo_mensaje)
