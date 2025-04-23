import psycopg2

config = {
    "host": "localhost",
    "database": "phone",
    "user": "postgres",
    "password": "12345"
}

def ddd(name , phone):
    try: 
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("call deleting(%s , %s)" , (name, phone))
        print("success!")
    except (psycopg2.DatabaseError ,  Exception) as error:
        print("error")

name , phone = input("enter name: ") , input("enter phone: ")
ddd(name,phone)