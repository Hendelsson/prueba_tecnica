# Informe de Presentación de Resultados - Proceso ETL

## 1. Arquitectura de Datos y Arquetipo de la Aplicación

### 1.1 Arquitectura de Datos
El proceso ETL (Extracción, Transformación y Carga) desarrollado sigue una arquitectura modular y escalable. La arquitectura se compone de los siguientes componentes:

- **Fuente de Datos**: Archivo Excel (`Films_2.xlsx`) almacenado en Google Drive.
- **Extracción**: Lectura de las cinco tablas principales del archivo Excel utilizando Apache Spark.
- **Transformación**: 
  - Eliminación de duplicados.
  - Limpieza de nombres de columnas.
  - Filtrado y conversión de valores numéricos.
  - Normalización de datos en la columna `email`.
  - Reasignación de valores consecutivos en `rental_id`.
- **Carga**: Almacenamiento de los datos procesados en formato Parquet dentro de un subdirectorio `output` en Google Drive.
- **Observabilidad**: Integración de logs para monitoreo y detección de errores durante la ejecución del ETL.

### 1.2 Arquetipo de la Aplicación
La aplicación sigue una estructura orientada a objetos y modular, cumpliendo con los principios SOLID para garantizar mantenibilidad y escalabilidad. Se utilizan las siguientes tecnologías:
- **Google Colab**: Entorno de ejecución.
- **Apache Spark**: Procesamiento distribuido de datos.
- **Google Drive**: Almacenamiento de entrada y salida de datos.
- **Python**: Lenguaje de programación principal.
- **Pandas**: Complemento para exploración de datos.

---

## 2. Análisis Exploratorio de Datos

Se realizó un análisis exploratorio sobre las tablas extraídas para entender la estructura de los datos y detectar problemas de calidad. Algunos hallazgos incluyen:

- **Presencia de duplicados** en varias tablas.
- **Nombres de columnas con espacios innecesarios**.
- **Valores numéricos con caracteres no numéricos**, los cuales fueron limpiados.
- **Emails con caracteres especiales al final** (`\r`), los cuales fueron eliminados.
- **Distribución de datos**:
  - La tabla `film` contiene información sobre películas, con datos como duración (`length`) y calificación (`rental_rate`).
  - La tabla `rental` almacena información sobre alquileres, con `rental_id` reindexado de manera secuencial.
  - `customer` y `store` incluyen datos de clientes y tiendas respectivamente.

---

## 3. Preguntas de Negocio y Respuestas

Los datos procesados pueden responder diversas preguntas de negocio. A continuación, se presentan cinco preguntas junto con sus respuestas basadas en el análisis de los datos:

### 1. ¿Cuál es la película más alquilada?
   - **FLAMINGOS CONNECTICUT** es la película con mayor número de alquileres.

### 2. ¿Cuántos clientes únicos han realizado al menos un alquiler?
   - **599 clientes** han realizado al menos un alquiler.

### 3. ¿Cuál es la tienda con más alquileres?
   - La tienda con numero 2 tiene la mayor cantidad de alquileres registrados.

### 4. ¿Cuál es la duración promedio de los alquileres?
   - La duración promedio de los alquileres es de aproximadamente **4.53 días**.

### 5. ¿Cuál es la calificación (rating) más común entre las películas alquiladas?
   - La calificación más común es **PG-13**.

---

## 4. Conclusiones

Tras la implementación del proceso ETL, se obtuvieron las siguientes conclusiones:

1. **Limpieza y Transformación de Datos**: Se logró eliminar inconsistencias como duplicados, caracteres no deseados en valores numéricos y caracteres especiales en `email`.
2. **Eficiencia del ETL**: La arquitectura basada en Apache Spark permite escalar el procesamiento a volúmenes de datos mayores.
3. **Observabilidad**: La inclusión de logs en el proceso ETL permite monitorear el estado de ejecución y detectar errores en tiempo real.
4. **Potencial Analítico**: Con los datos procesados, es posible generar reportes de negocio clave, como tendencias de alquiler y análisis de clientes.
5. **Escalabilidad y Mantenibilidad**: Gracias a la aplicación de principios SOLID y modularidad, el ETL es fácil de mantener y escalar para futuras mejoras.


