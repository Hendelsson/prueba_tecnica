from google.colab import drive
import os
from pyspark.sql import SparkSession

from extraccion import Extraccion
from transformacion import Transformacion
from carga import Carga



# 2️⃣ Definir rutas de entrada y salida en Google Drive
base_path = "/content/drive/MyDrive/etl_project"
input_path = os.path.join(base_path, "Films_2.xlsx")
output_path = os.path.join(base_path, "output")

# Crear la carpeta de salida si no existe
if not os.path.exists(output_path):
    os.makedirs(output_path)

# 3️⃣ Iniciar sesión de Spark
spark = SparkSession.builder.appName("ETL_Main").getOrCreate()

# 4️⃣ Proceso ETL

## 🔸 Extracción
extraccion = Extraccion(input_path)
dataframes = extraccion.extraer_datos()

## 🔸 Transformación
transformacion = Transformacion()
dataframes = transformacion.transformar_datos(dataframes)

## 🔸 Carga
carga = Carga(base_path)
carga.cargar_datos(dataframes)

print("🚀 ETL completado exitosamente. Los archivos Parquet están en Google Drive en la carpeta 'etl_project/output'.")

