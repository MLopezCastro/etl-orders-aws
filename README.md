
# 🛠️ ETL de Órdenes de Compra + Análisis en AWS

Este proyecto implementa un pipeline **ETL (Extract, Transform, Load)** sobre un archivo CSV de órdenes de compra, aplicando limpieza y validación de datos con Python, y luego carga el resultado a **AWS S3** para ser consultado mediante **Amazon Athena**. Es ideal para automatizar reportes o análisis en la nube.

---

## 📁 Estructura del Proyecto

```

ecommerce/
├── data/
│   ├── raw/                 # CSV original sin limpiar
│   └── output/              # CSV limpio final
├── logs/
│   └── etl.log              # Log del proceso ETL
├── scripts/
│   └── etl\_functions.py     # Funciones auxiliares de limpieza
├── main.py                  # Script principal del ETL
├── requirements.txt         # Dependencias del proyecto
└── README.md                # Documentación del proyecto

````

---

## 🚀 Cómo ejecutar el pipeline

Asegurate de tener Python 3.10+ y las dependencias instaladas:

```bash
pip install -r requirements.txt
````

Luego corré el ETL:

```bash
python main.py --input data/raw/orders.csv --output data/output/orders_clean.csv
```

Esto va a:

1. Leer el CSV crudo.
2. Validar y limpiar los datos.
3. Exportar un nuevo archivo limpio en `data/output/`.
4. Dejar logs detallados del proceso en `logs/etl.log`.

---

## ☁️ Carga en AWS

Una vez generado el CSV limpio (`orders_clean.csv`), se cargó a **Amazon S3** en la ruta:

```
s3://marcelo-orders-bucket/data/orders_clean.csv
```

Luego, se creó una tabla externa en **Amazon Athena** apuntando al bucket:

```sql
CREATE EXTERNAL TABLE IF NOT EXISTS default.orders_clean (
  order_id BIGINT,
  order_date DATE,
  customer_id BIGINT,
  product_id BIGINT,
  product_name STRING,
  quantity BIGINT,
  unit_price DOUBLE,
  currency STRING,
  status STRING,
  total_amount DOUBLE
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES ('field.delim'=',')
LOCATION 's3://marcelo-orders-bucket/data/'
TBLPROPERTIES ('skip.header.line.count'='1');
```

---

## 🔎 Análisis con SQL en Athena

Una vez cargada la tabla, se realizaron consultas para analizar las ventas por estado:

```sql
SELECT status, SUM(total_amount) AS total_sales
FROM orders_clean
GROUP BY status;
```

🔹 Resultado:

| status   | total\_sales |
| -------- | ------------ |
| pending  | 49.99        |
| returned | 89.97        |
| shipped  | 39.98        |

---

## 🧰 Stack Tecnológico

* 🐍 **Python 3.10**

  * `pandas` para procesamiento de datos
  * `boto3` para conexión a AWS
  * `dateutil` para manejo de fechas
* ☁️ **Amazon S3** (almacenamiento en la nube)
* 📊 **Amazon Athena** (consultas SQL serverless)

---

## 📦 Dependencias

Listado en `requirements.txt`:

```
pandas==2.2.2
boto3==1.34.124
python-dateutil==2.9.0
```

Instalación:

```bash
pip install -r requirements.txt
```

---

## ✅ Resultado Final

* CSV limpio listo para análisis: `data/output/orders_clean.csv`
* Logs detallados del proceso: `logs/etl.log`
* Datos disponibles en S3 para ser consultados con Athena
* SQL en la nube sin necesidad de infraestructura propia

---

## 🧠 Autor

Marcelo Fabián López – Data Analyst
🔗 [LinkedIn](https://www.linkedin.com/in/marcelolopezcastro) | [GitHub](https://github.com/MLopezCastro)

```
