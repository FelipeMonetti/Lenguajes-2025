# Ejercicios (Listas)
# Ingresar notas hasta -1, calcular el promedio y cuántos están por debajo.
# Dada una lista de palabras, construir otra con las que tengan más de 5 letras.
notas = []

nota = int(input("Ingresa una nota: "))
promedio = 0
totalNotas = 0

while nota != -1:
    notas.append(nota)
    promedio += nota
    totalNotas += 1
    nota = int(input("Ingresa una nota: "))

print("Lista con todas las notas → ",notas)
resultadoPromedio = promedio / totalNotas
print("Promedio de las notas: ", resultadoPromedio)

debajo = 0
for n in notas:
    if n < resultadoPromedio:
        debajo += 1

print(f"Hay un total de {debajo} notas debajo del promedio")

print("\n-------------------------------\n")

palabras = ["mate", "botella", "termo", "llave", "casa", "rinoceronte"]
print(f"Lista de palabras original: {palabras}\n")

palabras5 = []
for p in palabras:
    if len(p) > 5:
        palabras5.append(p)

print(f"Lista con las palabras que tienen más de 5 letras: {palabras5}")
