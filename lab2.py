import numpy as np

# 1. Cargar dataset con numpy
# Nota: usecols selecciona columnas específicas. Ajusta según tu archivo CSV.
# Ejemplo: si el CSV tiene columnas [Grupo, Canción, Debut, Ranking]
# cargamos solo Debut (col 2) y Ranking (col 3).
data = np.genfromtxt("kpop_group_debut_astrology.csv", delimiter=",", skip_header=1, usecols=(2,3), dtype=float)

# 2. Mostrar dimensiones (filas, columnas)
print("Dimensiones (filas, columnas):", data.shape)
print("="*50)

# 3. Resumen estadístico de las columnas
# Columna 0 = Debut (año), Columna 1 = Ranking
for i, col_name in enumerate(["Debut", "Ranking"]):
    col = data[:, i]
    col = col[~np.isnan(col)]  # eliminar valores NaN

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

# 5. Ordenar resultados
# Ejemplo: ordenar por año de debut (columna 0)
ordenados_debut = data[np.argsort(data[:, 0])]
print("Debuts más antiguos (primeros 5):")
print(ordenados_debut[:5])
print("="*50)

print("Debuts más recientes (últimos 5):")
print(ordenados_debut[-5:])
print("="*50)