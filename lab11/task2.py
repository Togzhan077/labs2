import psycopg2

config = {
    "host": "localhost",
    "database": "phone",
    "user": "postgres",
    "password": "12345"
}

def upsert(new_name, new_phone):
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("call upsert(%s, %s)", (new_name, new_phone))
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
new_name, new_phone = input("Enter a new name: "), input("Enter a new phone: ")

upsert(new_name, new_phone)