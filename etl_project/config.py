import os

# Rutas de archivos
DRIVE_PATH = "/content/drive/MyDrive/etl_project"
INPUT_FILE = os.path.join(DRIVE_PATH, "Films_2.xlsx")
OUTPUT_FILE = os.path.join(DRIVE_PATH, "Films_Extracted.xlsx")

# Configuración de Spark
SPARK_APP_NAME = "ETL_Films"
