import csv
import json
import datetime
import sys
sys.stdout.reconfigure(encoding='utf-8')             # cambio la salida a UTF-8 (que incluye acentos y símbolos) para que se imprima correctamente
from pathlib import Path

dias_traduccion = {
"Monday": "Lunes",
"Tuesday": "Martes",
"Wednesday": "Miércoles",
"Thursday": "Jueves",
"Friday": "Viernes",
"Saturday": "Sábado",
"Sunday": "Domingo"
}
dias = {}
campeones = {}
campeones_finde_semana = {}
semanas_presentes = set()   # uso un conjunto para guardar las semanas unicas (año, semana) y asi evitar contar la misma semana más de una vez
entrenamientos_por_dia = {} 
total_registros = 0 

ruta_csv = Path ('C:/Users/Monetti/Desktop/Lenguajes/actividad_2.csv')

try:
    with ruta_csv.open('r', newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        # inicializo las variables para guardar la primera y ultima fecha
        primera_fecha = None
        ultima_fecha = None

        for fila in reader:
            try:
                timestamp_texto = fila['timestamp']
                objeto_datetime = datetime.datetime.strptime(timestamp_texto, "%Y-%m-%d %H:%M")     # parseo la fecha (string) a objeto datetime para poder trabajarla
                fecha = objeto_datetime.date()
                iso_year, iso_week, _ = fecha.isocalendar() # Guardo el numero de semana ISO (año, semana) para calcular promedios semanales
                semanas_presentes.add((iso_year, iso_week))


                # obtengo el dia en ingles y lo traduzco a español
                dia_en_ingles = objeto_datetime.strftime("%A")
                dia_de_la_semana = dias_traduccion[dia_en_ingles] 

                # actualizo el contador de entrenamientos por campeon
                nombre = fila['campeon']
                campeones[nombre] = campeones.get(nombre, 0) + 1

                # cuento el registro valido
                total_registros += 1

                # acumulo por dia y campeon para el JSON final
                if dia_de_la_semana not in entrenamientos_por_dia:
                    entrenamientos_por_dia[dia_de_la_semana] = {}

                por_dia = entrenamientos_por_dia[dia_de_la_semana]
                por_dia[nombre] = por_dia.get(nombre, 0) + 1

                # si el entrenamiento fue sábado o domingo, lo sumo al contador de fines de semana
                if dia_de_la_semana in ["Sábado", "Domingo"]:
                    campeones_finde_semana[nombre] = campeones_finde_semana.get(nombre, 0) + 1 # si el campeón ya está en el diccionario, le sumo 1; 
                                                                                               # sino existe todavía, devuelve 0 como base y después le sumo 1

                # actualizo la primera y la ultima fecha del dataset
                if primera_fecha is None or fecha < primera_fecha:
                    primera_fecha = fecha
                
                if ultima_fecha is None or fecha > ultima_fecha:
                    ultima_fecha = fecha

                # actualizo el contador de entrenamientos por dia de la semana         
                if dia_de_la_semana not in dias:
                    dias[dia_de_la_semana] = 0
                dias[dia_de_la_semana] += 1

                print(f"{dia_de_la_semana} — {fila['campeon']} — {fila['actividad']} — {fila['entrenador']}")

            except ValueError:
                print(f"Error en formato de fecha: {timestamp_texto}")          # valido el formato 
            except KeyError as c:
                print(f"Falta una columna en el CSV: {c}")                      # valido que las claves (columnas) existan o esten bien escritas en el archivo

# ---------------------------------------------- C Á L C U L O S  ---------------------------------------------------

    if primera_fecha and ultima_fecha:                                         # valido que los valores no sean 'None'
        dias_transcurridos = (ultima_fecha - primera_fecha).days            # utilizo el .days para quedarme con el valor entero de la fecha que es lo que quiero
        print(f"\nEntre el primer y el último entrenamiento pasaron {dias_transcurridos} días")
    else:
        print("\nNo se pudieron determinar las fechas (no hubo registros válidos).")

    # valido si hay datos cargados en el diccionario
    if dias:                            
        dias_max = max(dias.values())
        dias_mas_ocupados = []              # lista para guardar los dias con mas entrenamientos

        for dia, cantidad in dias.items():  # recorro el diccionario y me quedo con los días que tienen más entrenamientos
            if cantidad == dias_max:
                dias_mas_ocupados.append(dia)

        # elijo el 'titulo' segun si hay un solo dia o varios con los mismos valores
        if len (dias_mas_ocupados) == 1:   
            titulo = "Dia con más sesiones de entrenamiento →"
        else:
            titulo = "Dias con más sesiones de entrenamiento →"
        print(f"\n{titulo} {', '.join(dias_mas_ocupados)} ({dias_max} sesiones)\n")        # uso el join para unir los elementos de la lista 

        print("Días ordenados por cantidad de entrenamientos: ")
        for dia, cantidad in sorted(dias.items(), key=lambda x: x[1], reverse=True):   # ordeno por cantidad de entrenamientos
            print(f"{dia}: {cantidad}")

        # defino el orden 'normal' de los días para que se impriman de Lunes a Domingo
        orden_dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

        # calculo la cantidad total de semanas detectadas en el dataset (año_iso, semana_iso)
        total_semanas = len(semanas_presentes)

        # si no se detectó ninguna semana, muestro un mensaje y evito dividir por cero
        # (también podría manejarse con la excepción ZeroDivisionError, pero prefiero validarlo antes)
        if total_semanas == 0:
            print("\nNo se pudo calcular el promedio por día: no hay semanas detectadas.")
        else:
            print("\nPromedio de entrenamientos por cada día de la semana:")

            # Uso map + lambda para aplicar la misma operación (calcular promedio) a todos los dias de la lista
            promedios = list(map(lambda d: (d, dias.get(d, 0) / total_semanas), orden_dias))

            for d, prom in promedios:   # recorro la lista de tuplas generada con map para mostrar los promedios con 2 decimales
                print(f"{d}: {prom:.2f}")

        if campeones_finde_semana:
            max_fin_semana = max(campeones_finde_semana.values())   # obtengo la cantidad máxima de entrenamientos en fin de semana


            top_campeones_finde = []   # lista para guardar los campeones con más entrenamientos de fin de semana

            for c, cant in campeones_finde_semana.items():   # recorro cada campeón y su cantidad
                if cant == max_fin_semana:                 # si tiene la cantidad máxima
                    top_campeones_finde.append(c)          # lo agrego a la lista


            # elijo el 'titulo' según si hay un solo campeón o varios con los mismos valores
            if len(top_campeones_finde) == 1:
                titulo = "\nCampeón que más entrena los fines de semana →"
            else:
                titulo = "\nCampeones que más entrenan los fines de semana →"

            print(f"{titulo} {', '.join(top_campeones_finde)} ({max_fin_semana} sesiones)\n")
        else:
            print("\nNo se registraron entrenamientos en fines de semana.")


        max_entrenos = max(campeones.values())                           # obtengo el numero maximo de entrenamientos realizados por un campeon
        max_campeones = []                                                # lista para guardar los campeones con esa cantidad maxima

        for campeon, cantidad in campeones.items():   # recorro el diccionario y me quedo con los campeones que tienen más entrenamientos
            if cantidad == max_entrenos:
                max_campeones.append(campeon)

        # elijo el 'titulo' según si hay un solo campeón o varios con los mismos valores
        if len(max_campeones) == 1:
            titulo = "\nCampeón que más entrenó →"
        else:
            titulo = "\nCampeones que más entrenaron →"

        print(f"{titulo} {', '.join(max_campeones)} ({max_entrenos} sesiones)\n")  # uso join para unir los nombres en caso de empate
    else:
        print("No se encontraron registros validos en el archivo")

    # Creo la carpeta 'salida' si no existe, para guardar los archivos generados
    carpeta_salida = ruta_csv.parent / "salida"                     # Uso ruta_csv.parent para que 'salida' quede al lado del archivo de entrada
    carpeta_salida.mkdir(parents=True, exist_ok=True)               # creo la carpeta si no existe y no falla si está

    # defino la ruta del archivo de salida
    ruta_salida_csv = carpeta_salida / "campeones_cantidades.csv"

    # Si no hay datos, aviso y no genero archivo vacío por error
    if not campeones:
        print("No se generó el CSV de salida porque no hay datos de campeones")
    else:
        # Escribo un archivo CSV con la cantidad total de entrenamientos por campeon
        # Abro el CSV de salida en modo escritura (write),  newline='' evita filas en blanco
        with ruta_salida_csv.open("w", newline="", encoding="utf-8") as fout:
            writer = csv.writer(fout)

            # escribo columnas
            writer.writerow(["campeon", "cantidad"])

            # escribo filas y ordeno por cantidad descendente y si hay empate, por nombre ascendente: con un sorted con lambda
            for nombre, cant in sorted(campeones.items(), key=lambda x: (-x[1], x[0])):
                writer.writerow([nombre, cant])

            print(f"CSV generado con éxito → {ruta_salida_csv}")

        # armo la estructura pedida: total de registros y, por cada día, lista de {campeon, cantidad}
        por_dia_listas = {}

        for dia, conteos in entrenamientos_por_dia.items():
            # transformo el dict {campeon: cantidad} -> lista de dicts ordenada
            lista_ordenada = sorted(
                ({"campeon": c, "cantidad": cant} for c, cant in conteos.items()),
                key=lambda x: (-x["cantidad"], x["campeon"])
            )
            por_dia_listas[dia] = lista_ordenada

        salida_json = {
            "total_registros": total_registros,
            "por_dia": por_dia_listas
        }

        # escribo el archivo JSON con indentación y UTF-8
        ruta_salida_json = carpeta_salida / "resumen_entrenamientos_por_dia.json"
        with ruta_salida_json.open("w", encoding="utf-8") as fout:
            json.dump(salida_json, fout, ensure_ascii=False, indent=2)

        print(f"JSON generado con éxito → {ruta_salida_json}")

except FileNotFoundError:                                           # valido si no existe el archivo en esa ruta
    print(f"No se encontró el archivo en la ruta: {ruta_csv}")

finally:                                             # muestro mensaje final aunque haya fallado algo, porque usando el with el archivo se cierra automáticamente
    print("\nEjecución finalizada.")