import psycopg2
import csv
config = {
    "host": "localhost",
    "database": "phone",
    "user": "postgres",
    "password": "12345"
}

def insert_by_csv(path):
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                with open(path, newline="", encoding='utf-8') as csvfile:
                    read = csv.DictReader(csvfile)
                    for row in read:
                        cur.execute("INSERT INTO phonebook(name, phone) VALUES(%s, %s)", (row["name"], row["phone"]))
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)
        
        
def insert_by_hand(name, phone):
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute("INSERT INTO phonebook(name, phone) VALUES(%s, %s)", (name, phone))
        print("Succes!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

election = input("Enter your action:\nC - csv\nH - hand insert")
if election == "C":
    path = input("Enter path: ")
    insert_by_csv(path)
elif election == "H":
    name, phone = input("Enter a name: "), input("Enter a phone: ")
    insert_by_hand(name, phone)
    