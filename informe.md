
# Informe técnico — Consolidación de reportes de ventas

**Para:** Gerencia de RetailAndina S. A. · **De:** Equipo de Business Intelligence  
**Fecha:** 20/10/2026 · **Asunto:** Primer análisis de los reportes de ventas (semana 39)

---

## Resumen ejecutivo

Se procedió al análisis de los reportes semanales de ventas de RetailAndina S. A., provenientes del sistema ERP, la plataforma de fidelización y el departamento de Finanzas, disponibles en formatos CSV, JSON y Excel. Mediante Python y R, se realizó la lectura e inspección de los datos y se calcularon indicadores comerciales. La venta promedio obtenida fue de 12.008 por sucursal y el ticket promedio general fue de 38,07. Guayaquil Centro registró las mayores ventas individuales, mientras que Sierra fue la región con mayor venta acumulada. Se recomienda estandarizar los formatos y validar la consistencia de los datos para facilitar futuros análisis y apoyar la toma de decisiones gerenciales.

## 1. ¿Los tres formatos contienen la misma información?

Realicé la lectura de los archivos CSV, JSON y Excel utilizando las bibliotecas correspondientes. Al comparar los resultados obtenidos en Python, comprobé que los tres archivos contienen cinco registros y cuatro columnas: `sucursal`, `region`, `ventas` y `clientes`. Además, los valores visualizados coincidieron en los tres formatos.

| Formato | Origen | Filas | Columnas | Lectura en código |
|---|---|---:|---:|---|
| CSV | ERP de sucursales | 5 | 4 | `pd.read_csv()` / `read_csv()` |
| JSON | API de fidelización | 5 | 4 | `pd.json_normalize()` / `fromJSON()` |
| Excel | Consolidado de finanzas | 5 | 4 | `pd.read_excel()` / `read_excel()` |

**¿La estructura interna del archivo (texto plano, anidada, binaria) cambia el contenido?**

Si bien los tres archivos almacenan los datos de manera diferente, su contenido es equivalente en este caso. CSV utiliza texto delimitado para organizar registros tabulares; JSON representa la información mediante objetos que pueden incluir estructuras anidadas; y Excel almacena los datos en hojas de cálculo. Por lo tanto, cambia la estructura interna del archivo, pero no la información recuperada después de su lectura y transformación.

## 2. Tipos de datos y calidad

Inspeccioné los tipos de datos inferidos por Python y R para verificar que fueran adecuados para el análisis estadístico. Las salidas de Python mostraron que las columnas numéricas se identificaron como enteros y las categóricas como texto.

| Variable | Tipo inferido (Python) | Tipo inferido (R) | Interpretación |
|---|---|---|---|
| `ventas` | `int64` | `num` o `int` | Variable numérica que representa las ventas registradas por sucursal. |
| `clientes` | `int64` | `num` o `int` | Variable numérica que indica la cantidad de clientes registrados. |
| `sucursal` | `str` | `character` | Variable categórica que identifica el nombre de cada sucursal. |
| `region` | `str` | `character` | Variable categórica que identifica la región de cada sucursal. |

**¿Qué habría indicado un dato sucio si, por ejemplo, `ventas` llegara como texto?**

Si la columna `ventas` se hubiera identificado como texto, podría indicar problemas de calidad, como símbolos monetarios, caracteres no numéricos o separadores inconsistentes. Esto dificultaría operaciones estadísticas como sumas y promedios. Por ello, sería necesario revisar, limpiar y convertir los valores a un tipo numérico antes de realizar el análisis.

## 3. Particularidades técnicas encontradas

**CSV:** La lectura fue directa, debido a que los datos ya estaban organizados en filas y columnas. Se pudieron visualizar los cinco registros y verificar sus cuatro variables, diferenciando correctamente las columnas numéricas de las categóricas.

**JSON:** Este formato puede contener estructuras anidadas, por lo que fue necesario utilizar `pd.json_normalize()` en Python para convertir los registros en una tabla. Después de la normalización, se obtuvo una estructura de cinco filas y cuatro columnas, equivalente a la de los otros formatos. En R se utilizó `jsonlite::fromJSON()` para importar los datos.

**Excel:** Se utilizó `pd.read_excel()` en Python y `readxl::read_excel()` en R para importar los datos de la hoja correspondiente al reporte de ventas. La lectura en Python mostró cinco registros y cuatro columnas, con los mismos valores observados en CSV y JSON.

**Variables categóricas:** En Python, las columnas `sucursal` y `region` se identificaron como `str`, mientras que en R se representan como `character`. Aunque cada lenguaje utiliza su propia clasificación de tipos, ambas permiten almacenar y analizar información categórica.

## 4. Indicadores para la reunión del lunes

Calculé los indicadores comerciales utilizando las funciones de análisis estadístico y agrupación de datos de Python y R. Los resultados permitieron comparar el desempeño de las sucursales y determinar la región con mayor volumen de ventas.

| Indicador | Valor |
|---|---|
| Venta promedio por sucursal | 12.008,00 |
| Ticket promedio (ventas ÷ clientes) | 38,07 |
| Sucursal con mayor venta | Guayaquil Centro — 15.200 |
| Sucursal con menor venta | Cuenca — 8.540 |
| Región con mayor venta total | Sierra — 30.860 |

La venta promedio por sucursal se obtuvo mediante la media de la columna `ventas`, con un resultado de 12.008. Para calcular el ticket promedio general, dividí la suma de las ventas entre la suma de los clientes, obteniendo aproximadamente 38,07.

Guayaquil Centro registró las mayores ventas individuales, mientras que Cuenca presentó el valor más bajo. Por regiones, Sierra acumuló 30.860, superando a Costa, que registró 29.180. Estos resultados permiten identificar diferencias en el desempeño comercial y proporcionan información útil para la toma de decisiones.

## 5. Conclusiones y recomendación

1. La lectura y comparación de los archivos CSV, JSON y Excel permitió comprobar que los tres reportes contienen cinco registros y cuatro columnas con valores coincidentes. A pesar de sus diferencias de almacenamiento, fue posible recuperar la misma información para el análisis comercial.

2. La inspección de los datos permitió reconocer correctamente las variables numéricas y categóricas. A partir de ellas, se obtuvo una venta promedio de 12.008 por sucursal y un ticket promedio general de 38,07. Guayaquil Centro registró las mayores ventas individuales, mientras que Sierra presentó el mayor volumen regional.

3. Se recomienda estandarizar los reportes mediante una estructura tabular común, con nombres de columnas y tipos de datos consistentes. CSV constituye una alternativa práctica para intercambiar información tabular sencilla debido a su facilidad de procesamiento en Python y R. Asimismo, es importante implementar controles de calidad para identificar datos incompletos, duplicados o incorrectos antes de utilizarlos en futuros análisis. Los resultados obtenidos describen únicamente las cinco sucursales y el período estudiado, por lo que no permiten realizar proyecciones de ventas futuras.
