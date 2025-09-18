# Ejercicios (Tuplas)
# Guardar coordenadas (x, y) en una tupla e imprimir la distancia al origen.
# Dada una lista de tuplas (nombre, edad), imprimir solo los mayores de 18.

import math
"""Importamos el modulo 'math' para poder calcular la raiz cuadrada"""
x = int(input("Ingresá la coordenada 'X': "))
y = int(input("\nIngresá la coordenada 'Y': "))
coordenadas = (x, y)


def potencia(base, exp=2):
    return base**exp


def origen(x, y):
    suma = potencia(x) + potencia(y)
    raiz = math.sqrt(suma)
    return raiz


print(
    f"\nLa distancia al origen de las coordenadas X = {x} e Y = {y} es: {round(origen(x,y), 4)}"        # Utilizo el round para truncar el resultado con 4 decimales
)


print("\n-------------------------------\n")


persona = [("Juan", 25), ("Pedro", 8), ("Juana", 18), ("Luis", 49)]         # Lista de tuplas
print("Dada la siguiente lista → ", persona)

print("\nLas personas que tienen más de 18 años son: ")
for p in persona:
    if p[1] > 18:
        print(p)
