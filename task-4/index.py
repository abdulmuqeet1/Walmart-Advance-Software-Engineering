import csv
import sqlite3
import os

data_dir = os.path.join(os.path.dirname(__file__), 'data')
os.makedirs(data_dir, exist_ok=True)

connect = sqlite3.connect('shipment_database.db')
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipping_data_0 (
        origin_warehouse TEXT,
        destination_store TEXT,
        product TEXT,
        on_time TEXT,
        product_quantity INTEGER,
        driver_identifier TEXT
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS shipping_data_1 (
        shipment_identifier TEXT,
        product TEXT,
        on_time TEXT,
        origin_warehouse TEXT,
        destination_store TEXT
    )
""")

connect.commit()
connect.close()

def insert_data(cursor):
    with open(os.path.join(data_dir, 'shipping_data_0.csv'), 'r') as file:
        file_reader = csv.reader(file)
        next(file_reader)
        for row in file_reader:
            origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier = row
            cursor.execute("INSERT INTO shipping_data_0 (origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier) VALUES (?, ?, ?, ?, ?, ?)",
                           (origin_warehouse, destination_store, product, on_time, product_quantity, driver_identifier))

    with open(os.path.join(data_dir, 'shipping_data_1.csv'), 'r') as file:
        file_reader = csv.reader(file)
        next(file_reader)
        for row in file_reader:
            shipment_identifier, product, on_time = row
            matching_rows = [r for r in shipping_data_2_rows if r[0] == shipment_identifier]
            if matching_rows:
                origin_warehouse, destination_store, driver_identifier = matching_rows[0][1], matching_rows[0][2], matching_rows[0][3]
                cursor.execute("INSERT INTO shipping_data_1 (shipment_identifier, product, on_time, origin_warehouse, destination_store) VALUES (?, ?, ?, ?, ?)",
                                (shipment_identifier, product, on_time, origin_warehouse, destination_store))

    with open(os.path.join(data_dir, 'shipping_data_2.csv'), 'r') as file:
        file_reader = csv.reader(file)
        next(file_reader)
        shipping_data_2_rows = [row for row in file_reader]

if __name__ == "__main__":
    conn = sqlite3.connect('shipment_database.db')
    cursor = conn.cursor()

    insert_data(cursor)

    conn.commit()
    conn.close()



