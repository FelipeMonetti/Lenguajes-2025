# piedra_papel_tijerav2.py
# Juego simple contra la computadora: versión modificada

import random

opciones = ["piedra", "papel", "tijera"]
opciones_rondas = [3, 5, 7]

print("¡Bienvenido! Vamos a jugar a Piedra, Papel o Tijera.")
print("Escribí tu jugada (piedra/papel/tijera).")

ronda = 1
puntos_usuario = 0
puntos_pc = 0
rondas_que_cuentan = 0
rondas_totales = 0

while rondas_totales not in opciones_rondas:                                      # verifica que el usuario ingrese lo que se pide
    rondas_totales = int(input("Elegí si se va a jugar al mejor de 3, 5 o 7: "))
    if rondas_totales not in opciones_rondas:
        print("Opción inválida. Probá otra vez.")

limite = (rondas_totales // 2) + 1

while rondas_que_cuentan < rondas_totales:                              # no es '<=' porque el break se ejecuta antes de llegar a que las rondas sean iguales
    print(f"\nRonda {ronda}")

    jugada_usuario = input("Tu jugada: ").strip().lower()

    if jugada_usuario not in opciones:
        print("Entrada no válida. Debe ser piedra, papel o tijera. Se debe repetir la ronda")
        continue # se debe repetir la ronda porque la entrada es inválida
    jugada_pc = random.choice(opciones)
    print(f"La computadora eligió: {jugada_pc}")

    if jugada_usuario == jugada_pc:
        print("Empate. Se debe repetir la ronda")
        continue # se debe repetir la ronda si es empate
    
    elif (
        (jugada_usuario == "piedra" and jugada_pc == "tijera") or
        (jugada_usuario == "papel" and jugada_pc == "piedra") or
        (jugada_usuario == "tijera" and jugada_pc == "papel")
    ):
        print("¡Ganaste la ronda!")
        puntos_usuario += 1

    else:
        print("Perdiste la ronda.")
        puntos_pc += 1
    ronda += 1
    rondas_que_cuentan += 1

    # Chequeo de corte

    if (puntos_usuario == limite) or (puntos_pc == limite):
        break
    print("\n=== Resultado parcial ===")
    print(f"Tus puntos: {puntos_usuario} | Puntos de la PC: {puntos_pc}")

print("\n=== Resultado final ===")
print(f"Tus puntos: {puntos_usuario} | Puntos de la PC: {puntos_pc}")

if puntos_usuario > puntos_pc:
    print("¡Ganaste el juego! 🎉")

elif puntos_usuario < puntos_pc:
    print("La computadora ganó el juego.")