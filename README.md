
# Análisis de Rendimiento de Automóviles

Este proyecto realiza un análisis de eficiencia de combustible en automóviles utilizando **Apache Spark** para el procesamiento por lotes y **Apache Kafka** para la transmisión de datos en tiempo real.

## Requisitos Previos

Antes de comenzar, asegúrate de tener los siguientes requisitos instalados:

1. **Java Development Kit (JDK)** 11 o superior
   - Descárgalo desde [Oracle JDK](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
   - Después de instalarlo, configura la variable de entorno `JAVA_HOME` con la ruta donde se instaló Java.

2. **Apache Spark** para el procesamiento de datos
   - Descarga [Apache Spark](https://spark.apache.org/downloads.html) y descomprime el archivo en una carpeta de tu elección.
   - Configura la variable de entorno `SPARK_HOME` apuntando a la carpeta de instalación de Spark.
   - Agrega `SPARK_HOME/bin` al `PATH` del sistema.

3. **Winutils.exe** (solo en Windows)
   - Descarga [winutils.exe](https://github.com/steveloughran/winutils) y colócalo en la carpeta `hadoop/bin`.
   - Configura la variable de entorno `HADOOP_HOME` apuntando a la carpeta de `hadoop`.

## Configuración del Entorno Virtual

Es recomendable usar un entorno virtual para manejar las dependencias del proyecto.

```bash
# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual (Linux/macOS)
source venv/bin/activate

# Activar el entorno virtual (Windows)
venv\Scripts\activate
```

## Instalación de Dependencias

Instala las librerías necesarias ejecutando:

```bash
pip install -r requirements.txt
```

Este comando instalará:
- `pyspark`: para el procesamiento de datos en Spark.
- `kafka-python`: para interactuar con Apache Kafka.

## Configuración de Apache Kafka

Para la transmisión de datos en tiempo real, necesitas tener una instancia de Apache Kafka en tu máquina local.

1. **Descargar Apache Kafka**
   - Descarga Kafka desde [Apache Kafka](https://kafka.apache.org/downloads) y descomprime el archivo en una carpeta de tu elección.

2. **Iniciar Zookeeper**  
   Navega a la carpeta de Kafka y ejecuta el siguiente comando:

   ```bash
   # En Windows
   .\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties

   # En Linux/macOS
   ./bin/zookeeper-server-start.sh ./config/zookeeper.properties
   ```

3. **Iniciar Kafka**  
   En otra terminal, ejecuta el siguiente comando:

   ```bash
   # En Windows
   .\bin\windows\kafka-server-start.bat .\config\server.properties

   # En Linux/macOS
   ./bin/kafka-server-start.sh ./config/server.properties
   ```

4. **Crear un Tópico de Kafka**  
   Puedes crear el tópico `real_time_topic` para la transmisión de datos:

   ```bash
   # En Windows
   .\bin\windows\kafka-topics.bat --create --topic real_time_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

   # En Linux/macOS
   ./bin/kafka-topics.sh --create --topic real_time_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1
   ```

## Colocar el Archivo de Datos

Asegúrate de que el archivo `car_data.csv` esté en la ruta especificada en el script de Spark (`C:/Users/usuario/Desktop/Pruebas/car_data.csv`). Si prefieres usar otra ruta, actualiza el código en el script.

## Ejecución de los Scripts

### 1. Procesamiento por Lotes en Apache Spark

Ejecuta el siguiente comando para iniciar el procesamiento de datos en Spark:

```bash
python scripts/spark_batch_processing.py
```

Este script cargará los datos de `car_data.csv`, realizará un análisis básico y guardará los datos procesados en formato Parquet.

### 2. Envío de Datos a Kafka

Para simular el envío de datos en tiempo real, ejecuta el siguiente comando:

```bash
python scripts/kafka_producer.py
```

Este script generará datos aleatorios y los enviará al tópico `real_time_topic` en Kafka.
