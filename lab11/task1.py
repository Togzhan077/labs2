import psycopg2

config = {
    "host": "localhost",
    "database": "phone",
    "user": "postgres",
    "password": "12345"
}

def get_record(pattern):
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("select get_record(%s)", (pattern,))
                result = cur.fetchall()
                print(result)
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
pattern = input("Enter a pattern: ")
get_record(pattern)
