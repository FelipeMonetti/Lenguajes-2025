# Ejercicios (Recorridos)
# Pedir una palabra y contar cuántas vocales tiene.
# Ingresar 4 palabras y mostrar únicamente las que contengan la letra 'r'.
# Ingresar palabras hasta escribir FIN; imprimir las que empiecen y terminen con la misma letra.

palabra = input("Ingresa una palabra: ").lower() 
vocales = 'aeiou'

tot = 0

for letra in palabra:         
    if letra in vocales:       
        tot +=1

print(f"La palabra tiene {tot} vocal/es.")

print("\n---------------------------------\n")

print("Ingresa 4 palabras: \n")
palabra1 = input("1:  ").lower()
palabra2 = input("2:  ").lower()
palabra3 = input("3:  ").lower()
palabra4 = input("4:  ").lower()

print("\nLas que contienen 'r' son: \n")
if ('r' in palabra1):
    print(palabra1)
if ('r' in palabra2):
    print(palabra2)
if ('r' in palabra3):
    print(palabra3)
if('r' in palabra4):
    print(palabra4)

print("\n---------------------------------\n")

lista_palabras = []

p = input("\nIngresa una palabra o 'FIN' para cortar: \n")

while p != "FIN":
    lista_palabras.append(p)
    p = input("Ingresa otra palabra: ")

print("\nPalabras que empiezan y terminan con la misma letra:\n")

for palabra in lista_palabras:
    if palabra[0].lower() == palabra[-1].lower(): 
        print(palabra)
