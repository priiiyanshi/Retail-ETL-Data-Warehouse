# Retail Data Warehouse & ETL Pipeline

## Overview
This project implements an end-to-end ETL pipeline that:
- Extracts retail sales data from CSV
- Transforms it using Python
- Loads into PostgreSQL
- Runs analytical SQL queries

## Tech Stack
- Python
- PostgreSQL
- Pandas
- SQL

## How to Run

1. Create PostgreSQL database:
   CREATE DATABASE retail_db;

2. Run schema.sql to create table.

3. Install dependencies:
   pip install -r requirements.txt

4. Run ETL:
   python etl/etl_pipeline.py

## Sample Analytics
- Monthly revenue
- Top selling products
- Revenue by category
