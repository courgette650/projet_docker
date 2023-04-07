import mysql.connector
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
import os

description = """
Customers API, l'API qui va changer votre vie ! 🚀 \n
Created with ❤️ by Aury Romain et Creurer Benjamin \n
Made with FastAPI, MariaDB and Docker
"""

tags_metadata = [
    {
        "name": "Base de données",
        "description": "Opérations avec la base de données. Initialisation, suppression, etc.",
    },
    {
        "name": "Customers",
        "description": "Operations avec les customers. Ajout, modification, suppression, etc.",
    },
]

user = os.environ.get('DATABASE_USER')
password = os.environ.get('DATABASE_PASSWORD')

config = {
    'host': 'mariadb',
    'port': 3306,
    'user': user,
    'password': password,
    'database': 'mydatabase'
}
app = FastAPI(description=description, title="Customers API", openapi_tags=tags_metadata , license_info={"name": "MIT", "url": "https://opensource.org/licenses/MIT"}, version="1.0.0")


@app.get("/", response_class=HTMLResponse, include_in_schema=False)
async def root(req: Request):
    return f"""
        <h1>Bonjour Monde !</h1>
        <p>Lien vers la doc : <a href=\"{req.base_url._url}docs\">Documentation</a></p> 
    """


@app.get("/customers", name="Get customers", description="Retourne tous les customers", tags=["Customers"])
async def get_customers():
    list_result: dict
    sql_query = "SELECT firstname, name, email FROM customers"
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    if cursor.description:
        # serialize results into JSON
        row_headers = [x[0] for x in cursor.description]
        rv = cursor.fetchall()
        list_result = []
        for result in rv:
            list_result.append(dict(zip(row_headers, result)))
    conn.close()
    return list_result


@app.post("/customers", name="Add customer", description="Ajoute un customer", tags=["Customers"])
async def add_customers(firstname: str, name: str, email: str):
    sql_query = "INSERT INTO customers (firstname, name, email) VALUES (%s, %s, %s)"
    customer_data = (firstname, name, email)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_query, customer_data)
    conn.commit()
    cursor.close()
    conn.close()


@app.put("/customers", name="Update a customer", description="Met à jour un customer", tags=["Customers"])
async def update_customers(customer_id: int, firstname: str, name: str, email: str):
    sql_query = "UPDATE customers SET firstname=%s, name=%s, email=%s WHERE id=%s"
    params = (firstname, name, email, customer_id)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_query, params)
    conn.commit()
    cursor.close()
    conn.close()


@app.delete("/customers/{id}", name="Delete a customer", description="Supprime un customer avec son id", tags=["Customers"])
async def delete_customers(id: int):
    sql_query = "DELETE FROM customers WHERE id=%s"
    params = (id,)
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_query, params)
    conn.commit()
    cursor.close()
    conn.close()


@app.get("/customers/{id}", name="Get customer by id", description="Retourne un customer à partir de son id", tags=["Customers"])
async def get_customer_by_id(id: int):
    list_result = {}

    sql_query = "SELECT firstname, name, email FROM customers WHERE id = %s"
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


@app.post("/init/customers", name="Init customers table", description="Initialise la base de données avec 10 customers fixe, supprime toutes les données existante", tags=["Base de données"])
async def init_customers():
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor(buffered=True)

    # Open and read the SQL file
    with open('init_db.sql', 'r') as sql_file:
        sql_script = sql_file.read()

    # Execute the SQL script
    for res in cursor.execute(multi=True, operation=sql_script):
        pass
    conn.commit()
    cursor.close()
    conn.close()
    return "OK"


@app.delete("/init/customers", name="Drop customers table", description="Supprime la table customers de la base de données", tags=["Base de données"])
async def delete_customers_table():
    sql_query = "DROP TABLE customers"
    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    conn.commit()
    cursor.close()
    conn.close()
    return "OK"
