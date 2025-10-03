# Ejercicios (Diccionarios)
# Leer nombres y notas hasta FIN y guardar en un diccionario. Luego mostrar:
# Promedio general, mejor estudiante, y los/as que están por debajo del promedio.
# Construir un diccionario {palabra: longitud} a partir de una frase.

diccionario = {}
notasTot = 0
AlumnosTot = 0
Promedio = 0
max = -1
mejorAlumno = ""
nombre = input("Ingrese un nombre completo: ")

while nombre.upper() != "FIN":
    """Lee nombres y notas y las guarda en un diccionario hasta leer'fin'"""
    diccionario[nombre] = int(input("Ingrese su nota: "))
    notasTot += diccionario[nombre]
    AlumnosTot += 1
    if diccionario[nombre] > max:
        max = diccionario[nombre]
        mejorAlumno = nombre
    nombre = input("Ingrese un nombre completo: ")

Promedio = notasTot / AlumnosTot
print(f"\nEl promedio general de las notas es de: {Promedio}\n")
print(f"El mejor estudiante de la clase es: {mejorAlumno}\n")

debajoPromedio = []
for i in diccionario:
    """Recorre el diccionario comparando notas con el promedio. Luego guarda en una lista"""
    if diccionario[i] < Promedio:
        debajoPromedio.append(i)

print(f"Los alumnos que están debajo del promedio son: {debajoPromedio}")

print("\n-------------------------------\n")

diccionario2 = {}

frase = input("Ingresa una frase: ")
palabras = frase.split()   # separa la frase por espacios y la guarda en palabra

for p in palabras:
    diccionario2[p] = len(p)

print("\nDiccionario generado a partir de la frase → ",diccionario2)


