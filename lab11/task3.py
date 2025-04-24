import psycopg2

conn = psycopg2.connect(
    dbname="phone", 
    user="postgres",  
    password="12345",
    host="localhost", 
    port="5432"
)

cur = conn.cursor()

user_names = ["Alice", "Bob", "Charlie"]
user_phones = ["1234567890", "2345678901", "3456789012"]

cur.execute("""
    CREATE OR REPLACE PROCEDURE insert_multiple_users(user_names TEXT[], user_phones TEXT[])
    LANGUAGE plpgsql AS $$
    DECLARE
        i INT;
    BEGIN
        -- Iterate over each element in the array (user_names and user_phones)
        FOR i IN 1..array_length(user_names, 1) LOOP
            -- Check if the user already exists, then update or insert accordingly
            IF EXISTS (SELECT 1 FROM phonebook WHERE name = user_names[i]) THEN
                UPDATE phonebook
                SET phone = user_phones[i]
                WHERE name = user_names[i];
            ELSE
                INSERT INTO phonebook (name, phone)
                VALUES (user_names[i], user_phones[i]);
            END IF;
        END LOOP;
    END;
    $$;
""")


cur.execute("""
    call insert_multiple_users(%s, %s);
""", (user_names, user_phones))

conn.commit()

cur.close()
conn.close()

print("Succes!")
