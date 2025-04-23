import psycopg2

config = {
    "host": "localhost",
    "database": "phone",
    "user": "postgres",
    "password": "12345"
}

def connect():
    try:
        with psycopg2.connect(**config) as conn:
            print("Connected")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
connect()

    


