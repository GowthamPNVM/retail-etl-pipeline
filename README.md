# Retail ETL Pipeline 🚀

A scalable, metadata-driven Retail ETL Pipeline built using Python, Pandas, and MySQL with production-style ETL engineering concepts.

This project simulates a real-world enterprise retail data pipeline that ingests synthetic transactional data, performs transformation and validation workflows, applies incremental processing using watermark metadata tracking, and loads optimized batch data into MySQL for analytics and reporting.

---

# 📌 Project Highlights

✅ Incremental ETL Processing  
✅ Metadata-Driven Watermark Tracking  
✅ Batch / Chunked Database Loading  
✅ Multi-Million Row Processing  
✅ Synthetic Data Engineering  
✅ Data Validation & Reconciliation  
✅ Referential Integrity Checks  
✅ SQL Analytics & KPI Reporting  
✅ Production Logging  
✅ Enterprise-Style Project Structure  

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | ETL Orchestration |
| Pandas | Data Processing |
| NumPy | Randomized Data Generation |
| Faker | Synthetic Data Creation |
| MySQL | Analytical Database |
| SQL | KPI & Analytics Queries |
| Logging | Pipeline Monitoring |
| ConfigParser | Externalized Configurations |

---

# 📂 Project Structure

```text
Retail-ETL-Pipeline/
│
├── config/
│   └── config.ini
│
├── data/
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── products.csv
│   │   ├── orders.csv
│   │   └── sales.csv
│   │
│   └── processed/
│       ├── customers_cleaned.csv
│       ├── products_cleaned.csv
│       ├── orders_cleaned.csv
│       └── sales_cleaned.csv
│
├── logs/
│   └── etl_pipeline.log
│
├── sql/
│   ├── schema.sql
│   ├── analytics.sql
│   ├── kpi_queries.sql
│   └── validation_queries.sql
│
├── src/
│   ├── generate_data.py
│   ├── extract.py
│   ├── transform.py
│   ├── incremental.py
│   ├── load.py
│   ├── pipeline.py
│   └── utils.py
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Pipeline Architecture

```text
Raw CSV Data
        ↓
Extraction Layer
        ↓
Transformation Layer
        ↓
Processed Data Layer
        ↓
Incremental Filtering
        ↓
Batch Loading Engine
        ↓
MySQL Analytical Database
        ↓
KPI & Analytics Queries
```

---

# 🔥 Features Implemented

## 1. Synthetic Data Generation

Generated large-scale retail datasets including:
- Customers
- Products
- Orders
- Sales

Implemented:
- randomized data generation
- referential integrity simulation
- scalable dataset creation
- append-based ingestion

---

## 2. Extraction Layer

Implemented:
- CSV ingestion
- selective column extraction
- schema-based reading
- reusable extraction utilities

---

## 3. Transformation Layer

Implemented:
- duplicate removal
- null handling
- data standardization
- datatype conversion
- business rule validation
- derived columns
- audit fields

---

## 4. Incremental ETL Processing

Implemented:
- metadata-driven watermark tracking
- incremental filtering
- stateful ingestion
- append-only source handling

Used:

```text
etl_metadata
```

table for checkpoint tracking.

---

## 5. Batch Loading Optimization

Implemented:
- chunked transactional inserts
- scalable database loading
- large-volume processing
- rollback handling

Optimized loading for:

```text
~2 million sales records
```

---

## 6. Logging & Monitoring

Implemented:
- centralized logging
- error tracking
- load monitoring
- ETL lifecycle logging

---

## 7. Data Validation & Reconciliation

Implemented:
- duplicate detection
- orphan record checks
- null validations
- referential integrity validation
- business rule validation

---

# 🗄️ Database Schema

Tables created:
- customers
- products
- orders
- sales
- etl_metadata

---

# 📊 KPI Queries

Implemented business KPI reporting queries:

- Total Revenue
- Total Orders
- Total Customers
- Average Order Value
- Monthly Revenue Trends
- Top Customers
- Top Products
- High Value Sales %
- Customer Rankings

---

# 📈 Advanced SQL Analytics

Implemented:
- joins
- aggregations
- ranking functions
- window functions
- analytical reporting queries

Example:

```sql
SELECT
    customer_id,
    COUNT(order_id) AS total_orders,
    RANK() OVER(
        ORDER BY COUNT(order_id) DESC
    ) AS customer_rank
FROM orders
GROUP BY customer_id;
```

---

# ✅ Validation Queries

Implemented:
- duplicate checks
- null checks
- orphan record validation
- future date validation
- referential integrity validation

---

# 🚀 How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/vsvasa/retail-etl-pipeline.git
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Database

Update:

```text
config/config.ini
```

Example:

```ini
[mysql]
host=localhost
user=root
password=your_password
database=retail_etl
```

---

## 5. Create Database Tables

Run:

```sql
schema.sql
```

---

## 6. Generate Data

```bash
python src/generate_data.py
```

---

## 7. Run ETL Pipeline

```bash
python src/pipeline.py
```

---

# 📌 Key Engineering Concepts Demonstrated

| Concept | Status |
|---|---|
| ETL Pipeline Engineering | ✅ |
| Incremental ETL | ✅ |
| Watermark Processing | ✅ |
| Metadata Tracking | ✅ |
| Batch Processing | ✅ |
| Chunked Inserts | ✅ |
| Large-Scale Data Handling | ✅ |
| Data Validation | ✅ |
| Referential Integrity | ✅ |
| SQL Analytics | ✅ |
| Window Functions | ✅ |
| Logging & Monitoring | ✅ |
| Error Handling | ✅ |
| Scalable Data Design | ✅ |

---

# 💡 Real-World Engineering Problems Solved

During development, solved:
- duplicate key handling
- schema drift issues
- datatype inconsistencies
- incremental synchronization problems
- large transaction timeouts
- MySQL connection drops
- chunked loading optimization
- data reconciliation challenges

---

# 📌 Resume Description

```text
Developed a scalable metadata-driven retail ETL pipeline using Python, Pandas, and MySQL with incremental ingestion, chunked transactional loading, audit tracking, data quality validation, analytical SQL reporting, and multi-million-row processing optimization.
```

---

# 🎯 Interview Topics Covered

This project demonstrates hands-on experience with:

- ETL Pipeline Development
- Incremental Processing
- Watermark Tracking
- Batch Processing
- Data Validation
- SQL Analytics
- Window Functions
- Referential Integrity
- Logging & Monitoring
- Scalable Data Engineering
- Metadata-Driven Pipelines
- Stateful ETL Systems

---

# 📷 Recommended README Screenshots

Add screenshots for:
- ETL pipeline logs
- MySQL tables
- KPI query outputs
- Project folder structure
- Incremental load execution

---

# 🔮 Future Enhancements

Planned upgrades:
- Apache Airflow orchestration
- PySpark transformation engine
- AWS S3 integration
- Docker containerization
- Kafka streaming ingestion
- Snowflake warehouse integration
- Data quality dashboards

---

# 👨‍💻 Author

Gowtham PNVM

---

# ⭐ GitHub Topics

```text
python
etl
mysql
pandas
data-engineering
incremental-etl
batch-processing
analytics
data-pipeline
sql
```