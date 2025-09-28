import math
import random

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
def genMensaje(codigos, probabilidades, N):
    msj = [random.choices(codigos, weights=probabilidades)[0] for _ in range(N)]
    return ''.join(msj)