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

- **Google Colab** (Para ejecutar el código en la nube)
- **Google Drive** (Para almacenar el archivo fuente y los resultados)


## **Cómo Ejecutar el ETL en Google Colab**

1. **Sube la carpeta `etl_project` a Google Drive** en la ubicación: `/content/drive/MyDrive `
2. **Abre Google Colab** y monta Google Drive con este código:


```python
from google.colab import drive
drive.mount('/content/drive')

```
3. **Ejecuta el siguiente comando:**
```python
!python3 "/content/drive/My Drive/etl_project/main.py"
```



## Resultados
Los datos transformados se guardan en formato **Parquet** en la carpeta `output/` dentro de `etl_project` en Google Drive.

# Justificación del Diseño del ETL

## Introducción

El diseño del ETL se basa en la necesidad de procesar datos de películas de manera eficiente, asegurando calidad, limpieza y transformaciones óptimas.

---
## **Elección de Tecnologías**

| Tecnología       | Justificación |
|-----------------|--------------|
| **Python 3** | Lenguaje versátil y compatible con bibliotecas de datos. |
| **Apache Spark (PySpark)** | Procesamiento eficiente de datos grandes en paralelo. |
| **Google Drive** | Almacenamiento accesible y fácil integración con Colab. |
| **Parquet** | Formato eficiente para almacenamiento y consultas rápidas. |

---

## **Diseño del ETL**

El diseño sigue un enfoque **modular y escalable**, permitiendo reutilización y mantenimiento sencillo.

###  **Módulos Principales**
1. **Extracción (`extraction.py`)**  
   - Lee datos desde un archivo Excel (`Films_2.xlsx`).
   - Ignora pestañas vacías o irrelevantes.

2. **Transformación (`transformation.py`)**  
   - **Elimina duplicados** en cada tabla clave.  
   - **Limpia encabezados** y valores numéricos con caracteres no deseados.  
   - **Corrige datos en la columna `rental_id`** generando valores consecutivos.  
   - **Elimina caracteres no deseados en `email`**.

3. **Carga (`load.py`)**  
   - Almacena los datos transformados en **Google Drive** en formato **Parquet**.

4. **Observabilidad (`observability.py`)**  
   - Registra eventos clave y errores.
   - Proporciona métricas de ejecución.

---

## **Ventajas del Diseño**

 **Escalabilidad:** Apache Spark permite manejar grandes volúmenes de datos.  
 **Flexibilidad:** Se pueden agregar nuevas transformaciones sin afectar la arquitectura.  
 **Eficiencia:** Uso de Parquet para optimizar almacenamiento y consultas.  
 **Reproducibilidad:** Se ejecuta fácilmente en Google Colab con Google Drive.  
 **Trazabilidad:** Módulos de observabilidad para depuración y análisis.

---

## **Conclusión**

El diseño modular del ETL permite procesar datos de manera eficiente, asegurando **calidad, limpieza y almacenamiento optimizado**. Su implementación en Google Colab y Google Drive lo hace accesible y fácil de ejecutar sin infraestructura adicional.



