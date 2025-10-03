# Escribir es_palindromo(cadena) que devuelva True si la cadena se lee igual al derecho y al revés (ignorar espacios y mayúsculas/minúsculas).
# Escribir contar_vocales(cadena) que retorne un diccionario con la cuenta de cada vocal.
# Escribir normalizar_palabras(frase) que retorne una lista de palabras sin signos de puntuación y en minúsculas.

import re
"""Importamos el modulo 're' para poder eliminar los signos de puntuación"""

def es_palindromo():
    """Comprueba si una cadena es palindromo y devuelve un booleano"""
    palabra = input("Ingresa una palabra: \n").lower().strip()
    i = 0
    j = len(palabra) - 1
    es_palindromo = True

    while i < j and es_palindromo:   
        if palabra[i] != palabra[j]:
            es_palindromo = False
        i += 1
        j -= 1

    return es_palindromo


print("\n¿Es palindromo? →", es_palindromo())

print("\n---------------------------------\n")

def contar_vocales():
    """Cuenta las vocales de una cadena y las guarda en un diccionario"""
    diccionario = {"a":0 , "e":0 , "i":0, "o":0, "u":0}
    palabra = input("Ingresa otra palabra: \n").lower()
    for i in palabra:
        if('a' in i):
            diccionario["a"] += 1
        elif('e' in i):
            diccionario["e"] += 1
        elif('i' in i):
            diccionario["i"] += 1
        elif('o' in i):
            diccionario["o"] += 1
        elif('u' in i):
            diccionario["u"] += 1
    return diccionario

print("\nCantidad de vocales → ",contar_vocales())

print("\n---------------------------------\n")

def normalizar_palabras():
    """Devuelve una lista con palabras en minusculas y sin signos de puntuacion"""
    lista = []
    frase = input("Ingresa una frase: \n").lower().strip()
    for i in range (4):
        sin_puntuacion = re.sub(r"[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ]", "", frase)
        lista.append(sin_puntuacion)
        frase = input("Ingresa otra frase: \n").lower().strip()
    sin_puntuacion = re.sub(r"[^a-zA-Z0-9áéíóúÁÉÍÓÚñÑ ]", "", frase)
    lista.append(sin_puntuacion)
    return lista

print("\nLista de palabras sin signos de puntuación y en minúscula → ", normalizar_palabras())