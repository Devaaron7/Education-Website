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
        table = '''CREATE TABLE {table}({c1} varchar(255) NOT NULL,{c2} varchar(255) NOT NULL)'''.format(table = table_name, c1 = column_1, c2 = column_2)
        cursor.execute(table)
        connection.commit()
        print("Table {table} Created".format(table = table_name))


    def delete_table(name):
        cursor.execute("DROP TABLE IF EXISTS {}".format(name))
        connection.commit()
        print("Table {} Deleted".format(name))
        


    def list_tables():
        cursor.execute('''SHOW TABLES''')
        total = cursor.fetchall()
        print(total)
        #connection.commit()

    def list_columns(table):
        cursor.execute('''SELECT NAME FROM {}'''.format(table))
        columns = cursor.fetchall()
        print(columns)

    
    #def insert_into_table(table_name, email, password):
    #    action = '''INSERT INTO {table}(email, password) VALUES ({e}, {p})'''.format(table = table_name, e = email, p = password)
    #    cursor.execute(action)
    #    connection.commit()
    #    print("Data inserted successfully: {e} / {p}".format(e = email, p = password))
    

    def insert_into_table(table_name, value):
        action = '''INSERT INTO {table}(NAME) VALUES ({v})'''.format(table = table_name, v = value)
        cursor.execute(action)
        connection.commit()
        print("Data inserted successfully: {v}".format(v = value))



    list_tables()

    insert_into_table("company", "Aaron")

    #create_table("users", "email", "password" )

    list_columns("company")

    #delete_table("users")

    #list_tables()

    

    

    #connection.commit()










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
