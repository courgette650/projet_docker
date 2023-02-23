import mysql.connector
from mysql.connector import (connection)
from fastapi import FastAPI, HTTPException

app = FastAPI()
config = {
    'host': 'mariadb',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'database': 'mydatabase'
}

@app.get("/")
async def root():
    return {"message": "Bonjour Monde !"}

@app.get("/customers")
async def get_customers():



    pass

@app.post("/customers")
async def add_customers(firstname: str, name: str, email: str):
    sql_query = "INSERT INTO customers (firstname, name, email) VALUES (%s, %s, %s)"
    customer_data = (firstname, name, email)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_query, customer_data)
    conn.commit()
    cursor.close()
    conn.close()
    pass

@app.put("/customers")
async def update_customers(customer_id: int, firstname: str, name: str, email: str):
    sql_query = "UPDATE customers SET firstname=%s, name=%s, email=%s WHERE id=%i"
    params = (firstname, name, email, customer_id)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_query, params)
    conn.commit()
    cursor.close()
    conn.close()

@app.delete("/customers")
async def delete_customers():
    pass

@app.get("/customers/{id}")
async def get_customer_by_email(id: int):
    list_result = {};
    
    sql_query = "SELECT firstname, name, email FROM customers WHERE id = %i"
    params = (id,)

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_query, params)
    if cursor.description:
        # serialize results into JSON
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        list_result = []
        for result in rv:
            list_result.append(dict(zip(row_headers, result)))
        
    conn.close()
    return list_result

