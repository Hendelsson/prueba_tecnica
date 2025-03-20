# Implementacion Detallada

## Descripción del Proyecto
Este proyecto implementa un proceso ETL (Extract, Transform, Load) utilizando **PySpark** en **Google Colab**, con almacenamiento de datos en **Google Drive**. El objetivo es extraer datos de un archivo Excel, limpiarlos y transformarlos siguiendo el **Modelo Entidad-Relación (MER)**, y almacenarlos en formato **Parquet** para su posterior análisis.

## Arquitectura
El proceso ETL sigue la siguiente arquitectura:
1. **Extracción**: Carga de datos desde un archivo Excel almacenado en Google Drive.
2. **Transformación**:
   - Eliminación de duplicados.
   - Limpieza de encabezados.
   - Filtrado de caracteres no numéricos en columnas específicas.
   - Normalización de identificadores secuenciales.
   - Limpieza de correos electrónicos.
3. **Carga**: Almacenamiento de los datos transformados en formato **Parquet** dentro de un subdirectorio en Google Drive.

## Requisitos
Para ejecutar este ETL, se requiere:
- **Google Colab** con acceso a Google Drive.
- Instalación de dependencias:
  ```python
  !pip install pyspark
  ```
- Archivo de datos: **Films_2.xlsx** en la carpeta `etl_project` dentro de Google Drive.

## Estructura del Proyecto
```
/etl_project
│── main.py              # Script principal que ejecuta el ETL
│── extracción.py        # Módulo de extracción de datos
│── transformación.py    # Módulo de transformación de datos
│── carga.py             # Módulo de carga de datos
│── utils.py             # Funciones auxiliares y configuración
│── output/              # Carpeta donde se almacenan los archivos Parquet
│── Films_2.xlsx         # Archivo fuente de datos
```

## Ejecución
Para ejecutar el proceso ETL en Google Colab:
1. **Montar Google Drive**:
   ```python
   from google.colab import drive
   drive.mount('/content/drive')
   ```
2. **Ejecutar el script principal**:
   ```python
   !python /content/drive/My Drive/etl_project/main.py
   ```

## Observabilidad
Se han integrado módulos de observabilidad que generan logs de cada paso del proceso. Los mensajes de estado indican:
- Inicio y fin del proceso ETL.
- Tablas extraídas correctamente.
- Transformaciones aplicadas con éxito.
- Errores y advertencias detectadas.

## Resultados
Los datos transformados se guardan en formato **Parquet** en la carpeta `output/` dentro de `etl_project` en Google Drive.

