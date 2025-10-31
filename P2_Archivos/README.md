# 🧠 Práctica 2 – Lenguajes 2025

Alumno: **Felipe Monetti**

---

## 🧾 Descripción

Este repositorio contiene un script en Python que analiza un archivo CSV con datos de entrenamientos semanales y genera distintos reportes y resúmenes.

El programa realiza las siguientes acciones principales:

- Traduce los días de la semana del inglés al español.  
- Cuenta la cantidad de entrenamientos por día.  
- Identifica el campeón con más entrenamientos totales.  
- Identifica el campeón con más entrenamientos en fines de semana.  
- Exporta los resultados a archivos en formato **CSV** y **JSON**.

---

## ▶️ Cómo ejecutarlo

1. Clonar el repositorio o descargar la carpeta `P2_Archivos`.  
2. Abrir una terminal en esa carpeta.  
3. Ejecutar el script con el siguiente comando:
```bash
   python script_act2.py
   ```
4. Los resultados se mostrarán en consola y también se guardarán en la carpeta de salida configurada dentro del código  
   (por ejemplo: `C:/Users/Monetti/Desktop/Lenguajes/salida/`).

---

## 📂 Archivos

### 📥 Entrada
- `actividad_2.csv` → contiene el registro original de entrenamientos (día, campeón, cantidad de sesiones, etc.)

### 📜 Script principal
- `script_act2.py` → código que analiza los datos, genera estadísticas y exporta los resultados

### 📤 Salida
- `campeones_cantidades.csv` → cantidad de sesiones por campeón  
- `resumen_entrenamientos_por_dia.json` → cantidad de entrenamientos por día de la semana  

---

## 💡 Notas

- El código utiliza manejo de excepciones (`try-except`) para detectar errores de lectura o escritura.  
- Asegurarse de tener el archivo de entrada (`actividad_2.csv`) disponible en la ruta especificada antes de ejecutar el programa.  
- Todos los resultados se imprimen en consola y se guardan automáticamente al finalizar la ejecución.

