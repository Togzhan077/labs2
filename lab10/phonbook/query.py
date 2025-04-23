import psycopg2

config = {
    "host": "localhost",
    "database": "phone",
    "user": "postgres",
    "password": "12345"
}

def select_order_by(obj, order):
    command = None
    if order == 0:
        command = f"SELECT id, name, phone FROM phonebook ORDER BY {obj}"
    else:
        command = f"SELECT id, name, phone FROM phonebook ORDER BY {obj} DESC"
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(command)
                result = cur.fetchall()
                print(result)
            

        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def select_by_name(name):
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM phonebook WHERE name = %s", (name,))
                result = cur.fetchall()
                print(result)
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def select_by_phone(phone):
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM phonebook WHERE phone = %s", (phone,))
                result = cur.fetchall()
                print(result)
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def select_by_id(id):
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT * FROM phonebook WHERE id = %s", (id,))
                result = cur.fetchall()
                print(result)
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def default_select():
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor()as cur:
                cur.execute("SELECT * FROM phonebook")
                result = cur.fetchall()
                print(result)
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

select = input("Choose mode:\nI - choose by id\nS - sorting\nN - choose by name\nP - choose py phone\nD - default select\n")
if select == 'S':
    ord = input("Order by: ")
    regime = int(input("Regime 0-ASC\n1-DESC\n"))
    select_order_by(ord, regime)
elif select == 'N':
    name = input("Name: ")
    select_by_name(name)
elif select == 'P':
    phone = input("Phone: ")
    select_by_phone(phone)
elif select == "I":
    id = int(input("ID: "))
    select_by_id(id)
else:
    default_select()