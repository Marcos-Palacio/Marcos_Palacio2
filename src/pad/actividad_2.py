
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Crear carpeta 'resultados' para almacenar archivos generados
carpeta_resultados = "resultados"
os.makedirs(carpeta_resultados, exist_ok=True)

# Diccionario donde almacenaremos los resultados de cada ejercicio
resultados = {}

### 📌 EJERCICIO 1: SUMA
print("Ejercicio 1: Sumar 5 + 3")
resultado_1 = 5 + 3
print(f"Resultado: {resultado_1}\n")
resultados["Ejercicio 1"] = [resultado_1]

### 📌 EJERCICIO 2: RESTA
print("Ejercicio 2: Restar 12 - 4")
resultado_2 = 12 - 4
print(f"Resultado: {resultado_2}\n")
resultados["Ejercicio 2"] = [resultado_2]

### 📌 EJERCICIO 3: MULTIPLICACIÓN
print("Ejercicio 3: Multiplicar 2 × 6")
resultado_3 = 2 * 6
print(f"Resultado: {resultado_3}\n")
resultados["Ejercicio 3"] = [resultado_3]

### 📌 EJERCICIO 4: DIVISIÓN
print("Ejercicio 4: Dividir 16 ÷ 2")
resultado_4 = 16 / 2
print(f"Resultado: {resultado_4}\n")
resultados["Ejercicio 4"] = [resultado_4]

### 📌 EJERCICIO 5: POTENCIACIÓN
print("Ejercicio 5: 10 elevado a la 2")
resultado_5 = 10 ** 2
print(f"Resultado: {resultado_5}\n")
resultados["Ejercicio 5"] = [resultado_5]

### 📌 EJERCICIO 6: RAÍZ CUADRADA
print("Ejercicio 6: Raíz cuadrada de 49")
resultado_6 = np.sqrt(49)
print(f"Resultado: {resultado_6}\n")
resultados["Ejercicio 6"] = [resultado_6]

### 📌 EJERCICIO 7: LOGARITMO NATURAL
print("Ejercicio 7: Logaritmo natural de 10")
resultado_7 = np.log(10)
print(f"Resultado: {resultado_7}\n")
resultados["Ejercicio 7"] = [resultado_7]

### 📌 EJERCICIO 8: SENO DE UN ÁNGULO
print("Ejercicio 8: Seno de 90° (π/2 radianes)")
resultado_8 = np.sin(np.pi / 2)
print(f"Resultado: {resultado_8}\n")
resultados["Ejercicio 8"] = [resultado_8]

### 📌 EJERCICIO 9: COSENO DE UN ÁNGULO
print("Ejercicio 9: Coseno de 180° (π radianes)")
resultado_9 = np.cos(np.pi)
print(f"Resultado: {resultado_9}\n")
resultados["Ejercicio 9"] = [resultado_9]

### 📌 EJERCICIO 10: TANGENTE DE UN ÁNGULO
print("Ejercicio 10: Tangente de 45° (π/4 radianes)")
resultado_10 = np.tan(np.pi / 4)
print(f"Resultado: {resultado_10}\n")
resultados["Ejercicio 10"] = [resultado_10]

### 📌 EJERCICIO 11: EXPONENCIAL
print("Ejercicio 11: e elevado a la 1")
resultado_11 = np.exp(1)
print(f"Resultado: {resultado_11}\n")
resultados["Ejercicio 11"] = [resultado_11]

### 📌 EJERCICIO 12: SUMA DE LOS PRIMEROS 10 NÚMEROS
print("Ejercicio 12: Suma de los primeros 10 números naturales")
resultado_12 = sum(range(1, 11))
print(f"Resultado: {resultado_12}\n")
resultados["Ejercicio 12"] = [resultado_12]

### 📌 EJERCICIO 13-18: ESTADÍSTICAS SOBRE UNA LISTA DE NÚMEROS
datos = [3, 7, 2, 9, 10]
print(f"Lista de datos: {datos}")

resultados["Ejercicio 13"] = [np.mean(datos)]   # Media
resultados["Ejercicio 14"] = [np.median(datos)] # Mediana
resultados["Ejercicio 15"] = [np.std(datos)]    # Desviación estándar
resultados["Ejercicio 16"] = [np.var(datos)]    # Varianza
resultados["Ejercicio 17"] = [max(datos)]       # Máximo
resultados["Ejercicio 18"] = [min(datos)]       # Mínimo

# Imprimir resultados de estadísticas
for i in range(13, 19):
    print(f"Ejercicio {i}: {resultados[f'Ejercicio {i}'][0]}")

print("\n")

### 📌 EJERCICIO 19: HISTOGRAMA CON DIFERENTES BINS
data = np.random.randn(1000)

plt.figure()
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title("Histograma con diferentes bins")
ruta_histograma_bins = os.path.join(carpeta_resultados, "histograma_bins.png")
plt.savefig(ruta_histograma_bins)
plt.close()

print(f"Ejercicio 19: Histograma guardado en {ruta_histograma_bins}\n")
resultados["Ejercicio 19"] = ["Ver gráfico: histograma_bins.png"]

### 📌 EJERCICIO 20: HISTOGRAMA CON LÍNEA DE MEDIA
plt.figure()
plt.hist(data, bins=30, alpha=0.7, color='red', edgecolor='black')
plt.axvline(data.mean(), color='black', linestyle='dashed', linewidth=2)
plt.title("Histograma con línea de media")
ruta_histograma_media = os.path.join(carpeta_resultados, "histograma_media.png")
plt.savefig(ruta_histograma_media)
plt.close()

print(f"Ejercicio 20: Histograma guardado en {ruta_histograma_media}\n")
resultados["Ejercicio 20"] = ["Ver gráfico: histograma_media.png"]

### 📌 EJERCICIO 21: GENERAR ARCHIVO EXCEL
ruta_excel = os.path.join(carpeta_resultados, "resultados_ejercicios.xlsx")
df = pd.DataFrame(dict([(k, pd.Series(v)) for k, v in resultados.items()]))
df.to_excel(ruta_excel, index=False, engine='openpyxl')

print(f"Ejercicio 21: Archivo Excel guardado en {ruta_excel}\n")
resultados["Ejercicio 21"] = ["Archivo Excel generado correctamente"]

print("✅ Todos los ejercicios se ejecutaron correctamente y los archivos se guardaron en la carpeta 'resultados/'.")
