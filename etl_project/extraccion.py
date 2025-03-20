from pyspark.sql import SparkSession
import pandas as pd

class Extraccion:
    def __init__(self, input_path):
        """Inicializa la clase con la ruta del archivo Excel."""
        self.input_path = input_path
        self.spark = SparkSession.builder.appName("ETL_Extraccion").getOrCreate()

    def extraer_datos(self):
        """Extrae los datos de todas las pestañas del archivo Excel, ignorando las vacías."""
        # Cargar todas las hojas del Excel en un diccionario de DataFrames de Pandas
        xls = pd.ExcelFile(self.input_path)
        dataframes = {}

        for sheet_name in xls.sheet_names:
            df = pd.read_excel(self.input_path, sheet_name=sheet_name)

            # Omitir pestañas vacías
            if df.empty:
                print(f"⚠️ La pestaña '{sheet_name}' está vacía y será ignorada.")
                continue
            
            # Convertir DataFrame de Pandas a DataFrame de Spark
            spark_df = self.spark.createDataFrame(df)
            dataframes[sheet_name] = spark_df
            print(f"✅ Datos extraídos de la pestaña: {sheet_name}")

        return dataframes
