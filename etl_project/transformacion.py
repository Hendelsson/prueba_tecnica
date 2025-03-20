from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, when, expr, monotonically_increasing_id
from pyspark.sql.types import IntegerType

class Transformacion:
    def __init__(self):
        self.spark = SparkSession.builder.appName("ETL_Transformacion").getOrCreate()

    def eliminar_duplicados(self, df, primary_key):
        """Elimina duplicados basados en la clave primaria."""
        return df.dropDuplicates([primary_key])

    def limpiar_encabezados(self, df):
        """Elimina espacios en blanco al inicio y al final de los nombres de columnas."""
        for col_name in df.columns:
            df = df.withColumnRenamed(col_name, col_name.strip())
        return df

    def limpiar_numeros(self, df, columnas_a_limpiar):
        """Conserva solo los números en las columnas especificadas."""
        for col_name in columnas_a_limpiar:
            if col_name in df.columns:
                df = df.withColumn(col_name, regexp_replace(col(col_name).cast("string"), "\\D", "").cast(IntegerType()))
        return df

    def limpiar_email(self, df):
        """Identifica emails con '\r' al final y elimina los últimos 2 caracteres."""
        if "email" in df.columns:
            df = df.withColumn("email", 
                when(col("email").endswith("\r"), expr("substring(email, 1, length(email)-2)"))
                .otherwise(col("email"))
            )
        return df

    def reenumerar_rental_id(self, df):
        """Genera una nueva columna rental_id con valores consecutivos."""
        if "rental_id" in df.columns:
            df = df.withColumn("rental_id", monotonically_increasing_id() + 1)
        return df

    def transformar_datos(self, dataframes):
        """Aplica transformaciones a los DataFrames."""
        
        columnas_a_limpiar = ["film_id", "release_year", "rental_rate", "length",
                              "replacement_cost", "num_voted_users", "store_id"]

        # Limpiar encabezados de todas las tablas
        for tabla in dataframes:
            dataframes[tabla] = self.limpiar_encabezados(dataframes[tabla])

        # Aplicar limpieza de números, emails y eliminación de duplicados
        for tabla in dataframes:
            dataframes[tabla] = self.limpiar_numeros(dataframes[tabla], columnas_a_limpiar)
            dataframes[tabla] = self.limpiar_email(dataframes[tabla])

        # Renumerar rental_id en la tabla rental
        if "rental" in dataframes:
            dataframes["rental"] = self.reenumerar_rental_id(dataframes["rental"])

        # Eliminar duplicados en cada tabla
        dataframes["customer"] = self.eliminar_duplicados(dataframes["customer"], "customer_id")
        dataframes["store"] = self.eliminar_duplicados(dataframes["store"], "store_id")
        dataframes["film"] = self.eliminar_duplicados(dataframes["film"], "film_id")
        dataframes["rental"] = self.eliminar_duplicados(dataframes["rental"], "rental_id")
        dataframes["inventory"] = self.eliminar_duplicados(dataframes["inventory"], "inventory_id")

        return dataframes

