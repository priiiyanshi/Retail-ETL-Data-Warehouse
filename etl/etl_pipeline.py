import pandas as pd
import psycopg2

DB_CONFIG = {
    "database": "retail_db",
    "user": "postgres",
    "password": "yourpassword",
    "host": "localhost",
    "port": "5432"
}

def run_etl():
    df = pd.read_csv("data/sales.csv")

    df["total_amount"] = df["quantity"] * df["price"]
    df["order_date"] = pd.to_datetime(df["order_date"])

    conn = psycopg2.connect(**DB_CONFIG)
    cur = conn.cursor()

    for _, row in df.iterrows():
        cur.execute("""
            INSERT INTO fact_sales 
            (order_id, customer_id, product, category, quantity, price, total_amount, order_date)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (order_id) DO NOTHING;
        """, (
            row.order_id,
            row.customer_id,
            row.product,
            row.category,
            row.quantity,
            row.price,
            row.total_amount,
            row.order_date
        ))

    conn.commit()
    cur.close()
    conn.close()

    print("ETL completed successfully!")

if __name__ == "__main__":
    run_etl()
