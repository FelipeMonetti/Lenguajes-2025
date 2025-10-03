# Programa de calificaciones: leer (nombre, nota) hasta FIN y luego mostrar: promedio, mediana, mejor y peor nota, y un informe ordenado por nombre.
import statistics

diccionario = {}
notasTot = 0
AlumnosTot = 0
Promedio = 0
mejorNota = -1
peorNota = 11
nombre = input("Ingrese un nombre: ")

while nombre.upper() != "FIN":
    """Lee nombres y notas y las guarda en un diccionario hasta leer'fin'"""
    diccionario[nombre] = int(input("Ingrese su nota: "))
    notasTot += diccionario[nombre]
    AlumnosTot += 1
    if diccionario[nombre] > mejorNota:
        mejorNota = diccionario[nombre]
    if diccionario [nombre] < peorNota:
        peorNota = diccionario[nombre]
    nombre = input("Ingrese otro nombre: ")

if AlumnosTot == 0:         # valida si no se ingresaron alumnos
    print("No se ingresaron alumnos")
    exit()

Promedio = notasTot / AlumnosTot
print(f"\nEl promedio general de las notas es de: {round(Promedio, 3)}\n")

valores = list(diccionario.values())                # convierto los valores del diccionario en una lista para poder usar la libreria
mediana = statistics.median(valores)
print(f"La nota mediana de la clase es: {mediana}\n")

print(f"La mejor nota de la clase es: {mejorNota}\n")
print(f"La peor nota de la clase es: {peorNota}\n")

print("---Alumnos y sus notas ordenados alfabéticamente---")

for nombre in sorted(diccionario.keys()):
    print (nombre, diccionario[nombre])