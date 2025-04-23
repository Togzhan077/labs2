import psycopg2

config = {
    "host": "localhost",
    "database": "phone",
    "user": "postgres",
    "password": "12345"
}

def delete(id):
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("DELETE FROM phonebook WHERE id=%s", (id,))
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
id = input("Enter an id: ")
delete(id)