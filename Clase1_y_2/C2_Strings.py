# Ejercicios (Strings)
# Pedir una palabra y mostrarla en mayúsculas, minúsculas y title case.
# Pedir una frase y contar cuántas veces aparece cada vocal.
# Dada una frase, mostrar las 3 primeras y las 3 últimas letras usando slicing.
# Verificar si una palabra contiene la letra 'r'. (Tip: in)

palabra = input(str("Ingresa una palabra: "))
print(palabra.upper())
print(palabra.lower())
print(palabra.title())

print("\n---------------------------------\n")

frase = input(str("Ingresa una frase: "))

a = e = i = o = u = 0

for caracter in frase.lower():  
    if caracter == 'a':
        a += 1
    elif caracter == 'e':
        e += 1
    elif caracter == 'i':
        i += 1
    elif caracter == 'o':
        o += 1
    elif caracter == 'u':
        u += 1
        
print(f"A: {a}")
print(f"E: {e}")
print(f"I: {i}")
print(f"O: {o}")
print(f"U: {u}")

print("\n---------------------------------\n")

frase2 = "Python developer"
print(frase2)
print("Primeras tres letras: ", frase2[:3])
print("Ùltimas tres letras: ", frase2[-3:])

print("\n---------------------------------\n")

palabra2 = input(str("Ingresa otra palabra: "))

print ("Tiene 'r'? ",'r' in palabra2)

