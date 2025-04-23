import psycopg2
config = {
    "host": "localhost",
    "database": "phone",
    "user": "postgres",
    "password": "12345"
}

def create():
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("CREATE TABLE phonebook(id BIGSERIAL NOT NULL PRIMARY KEY, name VARCHAR(150) NOT NULL, phone VARCHAR(12) NOT NULL)")
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
create()