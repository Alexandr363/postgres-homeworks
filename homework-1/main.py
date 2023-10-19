"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


conn = psycopg2.connect(host='localhost',
                        database='north',
                        user='postgres',
                        password='admin')

with conn:
    with conn.cursor() as cur:
        with open('north_data/customers_data.csv', 'r',
                  encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                            (row[0], row[1], row[2]))
                cur.execute('SELECT * FROM customers')

with conn:
    with conn.cursor() as cur:
        with open('north_data/employees_data.csv', 'r',
                  encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                cur.execute('INSERT INTO employees VALUES '
                            '(%s, %s, %s, %s, %s, %s)',
                            (row[0], row[1], row[2], row[3], row[4], row[5]))
                cur.execute('SELECT * FROM employees')

with conn:
    with conn.cursor() as cur:
        with open('north_data/orders_data.csv', 'r',
                  encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                cur.execute('INSERT INTO orders VALUES '
                            '(%s, %s, %s, %s, %s)',
                            (row[0], row[1], row[2], row[3], row[4]))
                cur.execute('SELECT * FROM orders')
