import os
import psycopg2

def exec_statement(conn, stmt):
    try:
        with conn.cursor() as cur:
            cur.execute(stmt)
            row = cur.fetchone()
            conn.commit()
            if row: print(row[0])
    except psycopg2.ProgrammingError:
        return











def main():
    # Connect to CockroachDB
    #connection = psycopg2.connect(os.environ['DATABASE_URL'])
    connection = psycopg2.connect(
    host="free-tier11.gcp-us-east1.cockroachlabs.cloud",
    port=26257, 
    dbname="terra-hamster-556.defaultdb",
    user="dev_link", 
    password="7sHSHqWHzdQJUrFrFclaSg")


    cursor = connection.cursor()

    def create_table(table_name, column_1, column_2):
        table = '''CREATE TABLE {}({} VARCHAR(64),{} VARCHAR(64))'''.format(table_name, column_1, column_2)
        cursor.execute(table)
        print("Table {} Created".format(table_name))
        connection.commit()


    def delete_table(name):
        cursor.execute("DROP TABLE IF EXISTS {}".format(name))
        print("Table {} Deleted".format(name))
        connection.commit()


    def list_tables():
        cursor.execute('''SHOW TABLES''')
        total = cursor.fetchall()
        print(total)
        #connection.commit()


    def insert_into_table(table_name, email, password):
        action = '''INSERT INTO {}(EMAIL, PASSWORD) VALUES ({}, {})'''.format(table_name, email, password)
        cursor.execute(action)
        print("Data inserted successfully: {} / {}".format(email, password))
        connection.commit()



    #list_tables()

    #create_table("USERS", "email", "password" )

    
    #delete_table("USERS")

    insert_into_table("USERS", 'john@gmail.com', 'aligator13')










    #cursor.execute('''INSERT INTO USERS("john@gmail.com", "button")''')

    #cursor.execute('''INSERT INTO USERS(EMAIL, PASSWORD) VALUES ("john@gmail.com", "button")''')
    
    #cursor.execute('''SELECT * from USERS''')

    #result = cursor.fetchall()

    #for data in result:
    #    print(data)

    #Commit your changes in the database
    #connection.commit()
    
    #Closing the connection
    connection.close()

    #print("Action Complete")


if __name__ == "__main__":
    main()
