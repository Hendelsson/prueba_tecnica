from pyspark.sql import SparkSession
import os

class Carga:
    def __init__(self, base_path):
        """Inicializa la clase de carga con la ruta de salida en Google Drive."""
        self.spark = SparkSession.builder.appName("ETL_Carga").getOrCreate()
        self.output_path = os.path.join(base_path, "output")

        # Crear el directorio si no existe
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def guardar_parquet(self, df, nombre_tabla):
        """Guarda un DataFrame en formato Parquet en Google Drive."""
        ruta_completa = os.path.join(self.output_path, f"{nombre_tabla}.parquet")
        df.write.mode("overwrite").parquet(ruta_completa)
        print(f"✅ Datos de {nombre_tabla} guardados en: {ruta_completa}")

    def cargar_datos(self, dataframes):
        """Guarda todos los DataFrames en formato Parquet."""
        for nombre_tabla, df in dataframes.items():
            self.guardar_parquet(df, nombre_tabla)
