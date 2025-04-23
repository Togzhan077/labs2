import psycopg2

config = {
    "host": "localhost",
    "database": "phone",
    "user": "postgres",
    "password": "12345"
}

def update_by_phone(old_phone, new_phone):
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE phonebook SET phone=%s WHERE phone=%s", (new_phone, old_phone))
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
def update_by_id(id, new_phone):
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE phonebook SET phone=%s WHERE id=%s", (new_phone, id))
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
action = input("Enter your action:\nP - by phone\nI - by id")
if action=="P":
    old_phone, new_phone = input("Enter a old phone: "), input("Enter a new_phone: \n")
    update_by_phone(old_phone, new_phone)
elif action=="I":
    id, new_phone = input("Enter an id: \n"), input("Enter a new phone: \n")
    update_by_id(id, new_phone)