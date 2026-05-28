# E-Commerce Inventory Data Pipeline

## Business Problem
The company requires real-time visibility into third-party supplier inventory to prevent stockouts and track total capital exposure. Manual checks are inefficient and prone to human error.

## Solution Architecture
This project is a localized ETL (Extract, Transform, Load) pipeline that automates inventory tracking and simulates real-time sales deductions.

* **Data Extraction:** Python script connects to a live REST API (`dummyjson`) to fetch current supplier inventory data via JSON payloads.
* **Data Storage:** Raw data is parsed, normalized, and loaded into a local SQLite relational database.
* **Data Transformation (SQL):** SQL queries are executed to filter out noise and isolate critical business metrics (e.g., items with stock < 10).
* **Business Intelligence:** A Power BI dashboard connects directly to the SQLite database via ODBC to visualize Total Inventory Value and actionable Restock Alerts.
* **Event Simulation:** A secondary Python script simulates real-time storefront sales, executing `UPDATE` queries on the database to demonstrate dynamic data flow.

## Tech Stack
* **Backend Engine:** Python (`requests`, `sqlite3`, `random`)
* **Database:** SQLite / SQL
* **Visualization:** Power BI Desktop (`.pbix`)
* **Data Format:** JSON / REST API

## Repository Contents
* `fetch_inventory.py`: API connection and database insertion logic.
* `analyze_inventory.py`: SQL query execution for low-stock alerts.
* `mock_amazon_sale.py`: Simulates a webhook/sale event altering the database.
* `Ecom_Data_Pipeline.pbix`: The Power BI dashboard file containing the KPI visuals.
* `requirements.txt`: Python environment dependencies.
