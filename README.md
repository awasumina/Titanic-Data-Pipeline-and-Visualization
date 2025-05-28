# 🚢 Titanic Data Pipeline: Gender-Based Survival Analysis using PostgreSQL and Airbyte

This project demonstrates an end-to-end data engineering workflow using the famous Titanic dataset. The main objective is to ingest the dataset into PostgreSQL, sync it across databases using Airbyte, apply SQL transformations, and analyze survival rates based on gender.

---

## 📦 Dataset Overview

The dataset contains passenger details including:
- `passenger_id`
- `survived` (1 = survived, 0 = not survived)
- `pclass` (passenger class)
- `name`
- `sex`
- `age`
- `fare`

Example records:

| passenger_id | survived | pclass | name  | sex    | age  | fare  |
|--------------|----------|--------|-------|--------|------|-------|
| 1            | 0        | 3      | John  | male   | 22.0 | 7.25  |
| 2            | 1        | 1      | Mary  | female | 38.0 | 71.28 |
| 3            | 1        | 3      | Anna  | female | 26.0 | 7.92  |
| 4            | 0        | 1      | Mark  | male   | 35.0 | 53.10 |
| 5            | 1        | 3      | Emily | female | 21.0 | 8.05  |

---

## 🛠️ Tools Used

- **PostgreSQL** – Database to store raw and transformed data
- **Airbyte** – Data integration platform to sync PostgreSQL ➝ PostgreSQL
- **SQL** – To perform survival rate transformation and aggregation
- **Python** – For data ingestion

---

## 🔁 ETL Workflow

1. **Extract** Titanic data from Kaggle.
2. **Load** into a source PostgreSQL database (`titanic_raw`).
3. **Sync** to another PostgreSQL database (`titanic_transformed`) using Airbyte.
4. **Transform** using SQL queries to compute gender-based survival rates.
5. **Verify** and **interpret** the transformed output.

---

## 📈 Interpretation

* **Male** passengers had a **survival rate of 18.9%**, indicating that most did not survive.
* **Female** passengers had a **survival rate of 74.2%**, showing a significantly higher chance of survival.

This result reflects historical accounts of evacuation priorities (e.g., "women and children first").
