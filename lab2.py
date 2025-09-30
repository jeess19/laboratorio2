import numpy as np
import os

# 0. Verificar que el archivo existe en la ruta actual
csv_file = "kpop_group_debut_astrology.csv"
if not os.path.exists(csv_file):
    raise FileNotFoundError(f"No se encontró el archivo CSV: {csv_file}")

# 1. Cargar dataset con numpy
# Ajusta usecols según las columnas numéricas reales en tu CSV
# Ejemplo: Debut (col 2), Ranking (col 3)
data = np.genfromtxt(csv_file, delimiter=",", skip_header=1, usecols=(2,3), dtype=float, invalid_raise=False)

# 2. Mostrar dimensiones (filas, columnas)
print("Dimensiones (filas, columnas):", data.shape)
print("="*50)

# 3. Resumen estadístico de las columnas
for i, col_name in enumerate(["Debut", "Ranking"]):
    col = data[:, i]
    col = col[~np.isnan(col)]  # eliminar valores NaN

    if col.size == 0:
        print(f" La columna '{col_name}' está vacía o no contiene números válidos.")
        print("="*50)
        continue

    print(f" Resumen de la columna '{col_name}':")
    print("Cantidad de datos:", col.size)
    print("Mínimo:", np.min(col))
    print("Máximo:", np.max(col))
    print("Media:", np.mean(col))
    print("Mediana:", np.median(col))
    print("Desviación estándar:", np.std(col, ddof=1))
    print("="*50)

# 4. Primeros y últimos registros
print("Primeros 5 registros:")
print(data[:5, :])
print("="*50)

print("Últimos 5 registros:")
print(data[-5:, :])
print("="*50)

# 5. Ordenar resultados por año de debut (columna 0)
col_debut = data[:, 0]
if col_debut.size == 0 or np.all(np.isnan(col_debut)):
    print(" No hay datos válidos para la columna 'Debut'. No se puede ordenar.")
else:
    ordenados_debut = data[np.argsort(col_debut)]
    print("Debuts más antiguos (primeros 5):")
    print(ordenados_debut[:5])
    print("="*50)

    print("Debuts más recientes (últimos 5):")
    print(ordenados_debut[-5:])
    print("="*50)