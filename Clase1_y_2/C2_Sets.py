# Ejercicios (Sets)
# Pedir dos listas de números (separados por espacios) y mostrar su intersección usando set.
# Eliminar duplicados de una lista manteniendo el orden (pista: usar un set auxiliar para vistos).

lista1 = input("Ingrese una lista de numeros separados por espacio: ").strip()
lista2 = input("Ingrese otra lista de numeros separados por espacio: ").strip()

lista1 = lista1.split()         # utilizo el split para separar los elementos de la lista
lista2 = lista2.split()

set1 = set(lista1)              # convierto las listas en conjuntos para poder hacer la operacion
set2 = set(lista2)

interseccion = set1 & set2      # realizo la interseccion entre ambos conjuntos

print("Interseccion de ambas listas → ", interseccion)

print("\n-------------------------------\n")

lista3 = input("Ingrese otra lista de numeros separada por espacio: ").split()

def eliminar_duplicados(lista3):
    vistos = set()
    resultado = []
    for num in lista3:
        if num not in vistos:                   # si el elemento no fue visto, es decir no esta duplicado, lo guardo
            resultado.append(num)                   # se mantiene el orden en que se ingresaron los elementos
            vistos.add(num)
    return resultado

listaSinDuplicados = eliminar_duplicados(lista3)        # guardo una nueva lista con el resultado de la funcion que elimina duplicados

print(f"Lista original → {lista3}")
print(f"Lista sin duplicados → {listaSinDuplicados}")

