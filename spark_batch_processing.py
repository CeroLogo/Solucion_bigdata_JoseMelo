from pyspark.sql import SparkSession
from pyspark.sql.functions import avg

# Iniciar la sesión de Spark
spark = SparkSession.builder.appName("CarPerformanceBatchProcessing").getOrCreate()

# Cargar el archivo CSV
file_path = "C:/Users/usuario/Desktop/Pruebas/car_data.csv"
df = spark.read.csv(file_path, header=True, inferSchema=True)

# Calcular el promedio de eficiencia de combustible en ciudad
avg_city_mpg = df.select(avg("city_mpg")).first()[0]
print(f"Promedio de eficiencia de combustible en ciudad: {avg_city_mpg}")

# Calcular el promedio de eficiencia de combustible en autopista
avg_highway_mpg = df.select(avg("highway_mpg")).first()[0]
print(f"Promedio de eficiencia de combustible en autopista: {avg_highway_mpg}")

# Mostrar el esquema del DataFrame
df.printSchema()

# Análisis Exploratorio de Datos (EDA)
# 1. Número total de filas
total_rows = df.count()
print(f"Número total de registros: {total_rows}")

# 2. Calcular el promedio de eficiencia de combustible en ciudad
df.select(avg("city_mpg")).show()

# 3. Calcular el promedio de eficiencia de combustible en autopista
df.select(avg("highway_mpg")).show()

# 4. Mostrar los primeros 5 registros limpios
df_clean = df.dropna()
df_clean.show(5)

# Almacenar los resultados procesados en formato Parquet
df_clean.write.mode("overwrite").parquet("C:/Users/usuario/Desktop/Pruebas/car_data_processed.parquet")
