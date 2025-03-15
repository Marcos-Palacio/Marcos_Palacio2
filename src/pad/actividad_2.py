
import os
import pad
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Definir la ruta correcta para guardar los resultados
carpeta_resultados = os.path.join(os.getcwd(), "src", "pad", "carpeta_resultados")

# Asegurar que la carpeta de resultados exista
os.makedirs(carpeta_resultados, exist_ok=True)

# Exportar los resultados a CSV y Excel
ruta_csv = os.path.join(carpeta_resultados, "resultados.csv")
ruta_excel = os.path.join(carpeta_resultados, "resultados.xlsx")

### Introducción y cálculos con los arrays de NumPy ###

# 1. Generar un array de NumPy con valores desde 10 hasta 29.
ej1 = np.arange(10, 30)
print("Ejercicio 1:", ej1)

# 2. Calcular la suma de todos los elementos en un array de NumPy de tamaño 10x10, lleno de unos.
ej2 = np.ones((10, 10)).sum()
print("Ejercicio 2:", ej2)

# 3. Producto elemento a elemento de dos arrays de tamaño 5 llenos de números aleatorios de 1 a 10.
ej3_a = np.random.randint(1, 11, 5)
ej3_b = np.random.randint(1, 11, 5)
ej3_result = ej3_a * ej3_b
print("Ejercicio 3:", ej3_result)

# 4. Generar una matriz aleatoria de 4x4 y asegurarse de que es invertible
while True:
    ej4 = np.random.randint(1, 10, (4, 4))  # Matriz con valores entre 1 y 9
    if np.linalg.det(ej4) != 0:  # Solo salimos del bucle si la matriz es invertible
        break

ej4_inv = np.linalg.inv(ej4)  # Ahora sí se puede calcular la inversa

print("Ejercicio 4: Matriz original")
print(ej4)
print("\nEjercicio 4: Matriz inversa")
print(ej4_inv)

# 5. Encontrar los valores máximo y mínimo en un array de 100 elementos aleatorios y mostrar sus índices.
ej5 = np.random.rand(100)
ej5_max, ej5_min = ej5.max(), ej5.min()
ej5_idx_max, ej5_idx_min = ej5.argmax(), ej5.argmin()
print("Ejercicio 5: Max:", ej5_max, "(índice:", ej5_idx_max, ") Min:", ej5_min, "(índice:", ej5_idx_min, ")")

### Broadcasting e indexado de Arrays ###

# 6. Crear un array de tamaño 3x1 y uno de 1x3, sumarlos con broadcasting para obtener un array de 3x3.
ej6_a = np.array([[1], [2], [3]])
ej6_b = np.array([1, 2, 3])
ej6_result = ej6_a + ej6_b
print("Ejercicio 6:\n", ej6_result)

# 7. Extraer una submatriz 2x2 de una matriz 5x5 con números aleatorios.
ej7 = np.random.randint(1, 100, (5, 5))
ej7_submatriz = ej7[1:3, 2:4]
print("Ejercicio 7:\n", ej7_submatriz)

# 8. Crear un array de ceros de tamaño 10 y cambiar los valores en los índices de 3 a 6 a 5.
ej8 = np.zeros(10)
ej8[3:7] = 5
print("Ejercicio 8:", ej8)

# 9. Invertir el orden de las filas en una matriz 3x3.
ej9 = np.random.randint(1, 100, (3, 3))
ej9_inv = ej9[::-1]
print("Ejercicio 9:\n", ej9_inv)

# 10. Seleccionar y mostrar elementos de un array aleatorio de tamaño 10 que sean mayores a 0.5.
ej10 = np.random.rand(10)
ej10_mayores = ej10[ej10 > 0.5]
print("Ejercicio 10:", ej10_mayores)

### Gráficos de dispersión, densidad y contorno ###

### EJERCICIO 11: Gráfico de dispersión con 100 puntos aleatorios
x_11 = np.random.rand(100)
y_11 = np.random.rand(100)
plt.figure()
plt.scatter(x_11, y_11, alpha=0.7, color='blue')
plt.title("Ejercicio 11: Gráfico de Dispersión")
ruta_dispersion = os.path.join(carpeta_resultados, "grafico_dispersion.png")
plt.savefig(ruta_dispersion)
plt.close()

### EJERCICIO 12: Gráfico de dispersión con función y = sin(x) + ruido
x_12 = np.linspace(-2 * np.pi, 2 * np.pi, 100)
y_12 = np.sin(x_12) + np.random.normal(0, 0.1, size=len(x_12))
plt.figure()
plt.scatter(x_12, y_12, alpha=0.7, color='red', label='y = sin(x) + ruido')
plt.plot(x_12, np.sin(x_12), color='black', linestyle='dashed', label='y = sin(x)')
plt.title("Ejercicio 12: Dispersión con función seno")
plt.legend()
ruta_seno = os.path.join(carpeta_resultados, "grafico_seno.png")
plt.savefig(ruta_seno)
plt.close()

### EJERCICIO 13: Gráfico de contorno usando meshgrid
x_13 = np.linspace(-2, 2, 100)
y_13 = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x_13, y_13)
Z = np.cos(X) + np.sin(Y)

plt.figure()
plt.contour(X, Y, Z, levels=20, cmap="coolwarm")
plt.colorbar()
plt.title("Ejercicio 13: Gráfico de Contorno")
ruta_contorno = os.path.join(carpeta_resultados, "grafico_contorno.png")
plt.savefig(ruta_contorno)
plt.close()

### EJERCICIO 14: Dispersión con 1000 puntos y colores según densidad
x_14 = np.random.rand(1000)
y_14 = np.random.rand(1000)
colors_14 = np.sqrt(x_14**2 + y_14**2)  # Color basado en distancia del origen

plt.figure()
plt.scatter(x_14, y_14, c=colors_14, cmap="viridis", alpha=0.7)
plt.colorbar(label="Densidad")
plt.title("Ejercicio 14: Dispersión con 1000 puntos y densidad")
ruta_densidad = os.path.join(carpeta_resultados, "grafico_densidad.png")
plt.savefig(ruta_densidad)
plt.close()

### EJERCICIO 15: Gráfico de contorno lleno (coloreado)
plt.figure()
plt.contourf(X, Y, Z, levels=20, cmap="coolwarm")
plt.colorbar()
plt.title("Ejercicio 15: Gráfico de Contorno Lleno")
ruta_contorno_f = os.path.join(carpeta_resultados, "grafico_contorno_lleno.png")
plt.savefig(ruta_contorno_f)
plt.close()

### EJERCICIO 16: Etiquetas y leyenda en el gráfico de dispersión (Ejercicio 12)
plt.figure()
plt.scatter(x_12, y_12, alpha=0.7, color='red', label='y = sin(x) + ruido')
plt.plot(x_12, np.sin(x_12), color='black', linestyle='dashed', label='y = sin(x)')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Ejercicio 16: Dispersión con etiquetas y leyenda")
plt.legend()
ruta_etiquetas = os.path.join(carpeta_resultados, "grafico_etiquetas.png")
plt.savefig(ruta_etiquetas)
plt.close()

### EJERCICIO 17: Histograma con datos distribuidos normalmente
data_17 = np.random.randn(1000)

plt.figure()
plt.hist(data_17, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title("Ejercicio 17: Histograma de distribución normal")
ruta_histograma = os.path.join(carpeta_resultados, "histograma_normal.png")
plt.savefig(ruta_histograma)
plt.close()

### EJERCICIO 18: Dos conjuntos de datos en un mismo histograma
data_18a = np.random.randn(1000) * 0.5 + 2  # Centro en 2
data_18b = np.random.randn(1000) * 0.5 + 5  # Centro en 5

plt.figure()
plt.hist(data_18a, bins=30, alpha=0.5, color='blue', label="Grupo 1")
plt.hist(data_18b, bins=30, alpha=0.5, color='red', label="Grupo 2")
plt.title("Ejercicio 18: Histogramas combinados")
plt.legend()
ruta_histogramas = os.path.join(carpeta_resultados, "histogramas_combinados.png")
plt.savefig(ruta_histogramas)
plt.close()

### EJERCICIO 19: Histograma con diferentes valores de bins
plt.figure()
plt.hist(data_17, bins=[10, 30, 50], alpha=0.7, color='purple', edgecolor='black')
plt.title("Ejercicio 19: Histogramas con diferentes bins")
ruta_histograma_bins = os.path.join(carpeta_resultados, "histograma_bins.png")
plt.savefig(ruta_histograma_bins)
plt.close()

### EJERCICIO 20: Histograma con línea de media
plt.figure()
plt.hist(data_17, bins=30, alpha=0.7, color='green', edgecolor='black')
plt.axvline(data_17.mean(), color='black', linestyle='dashed', linewidth=2)
plt.title("Ejercicio 20: Histograma con media")
ruta_histograma_media = os.path.join(carpeta_resultados, "histograma_media.png")
plt.savefig(ruta_histograma_media)
plt.close()

# Crear un diccionario con los resultados de los ejercicios
data = {
    "Ejercicio 1": [ej1.tolist()],  
    "Ejercicio 2": [ej2],  
    "Ejercicio 3": [ej3_result.tolist()],  
    "Ejercicio 4 - Matriz Original": [ej4.tolist()],  
    "Ejercicio 4 - Matriz Inversa": [ej4_inv.tolist()],  
    "Ejercicio 5 - Max": [ej5_max],  
    "Ejercicio 5 - Min": [ej5_min],  
    "Ejercicio 5 - Índice Max": [ej5_idx_max],  
    "Ejercicio 5 - Índice Min": [ej5_idx_min],  
    "Ejercicio 6": [ej6_result.tolist()],  
    "Ejercicio 7": [ej7_submatriz.tolist()],  
    "Ejercicio 8": [ej8.tolist()],  
    "Ejercicio 9": [ej9_inv.tolist()],  
    "Ejercicio 10": [ej10_mayores.tolist()],
      
}

### GUARDADO EN CSV Y EXCEL ###
df = pd.DataFrame.from_dict(data, orient="index").T
df.to_csv(ruta_csv, index=False)
df.to_excel(ruta_excel, index=False)

print("✅ Resultados almacenados en CSV y Excel correctamente.")
print("El paquete 'pad' está instalado y funcionando correctamente.")

