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
    
    connection = psycopg2.connect(
    host="free-tier11.gcp-us-east1.cockroachlabs.cloud",
    port=26257, 
    dbname="terra-hamster-556.defaultdb",
    user="dev_link", 
    password="7sHSHqWHzdQJUrFrFclaSg")

    cursor = connection.cursor()

    def create_table(table_name, primary_id, column_1, column_2):
        table = '''CREATE TABLE IF NOT EXISTS {table}(
        {p} int PRIMARY KEY, 
        {c1} varchar(255) NOT NULL,
        {c2} varchar(255))'''.format(table = table_name, p = primary_id, c1 = column_1, c2 = column_2)
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


    def list_columns(table):
        cursor.execute('''SELECT * FROM {}'''.format(table))
        columns = cursor.fetchall()
        for records in columns:
            print(records)
    

    def insert_into_table(table_name, primary_id, column_1, column_2):
        insert_script = '''INSERT INTO {table} (id, email, password) VALUES (%s, %s, %s)'''.format(table=table_name)
        insert_value = (primary_id, column_1, column_2)
        cursor.execute(insert_script, insert_value)
        connection.commit()
        print("Data inserted successfully: {p}, {c1}, {c2}".format(p = primary_id, c1 = column_1, c2 = column_2))





    #table = '''CREATE TABLE IF NOT EXISTS PEOPLE(
    #ID int PRIMARY KEY, 
    #NAME varchar(255) NOT NULL,
    #PASSWORD varchar(255))'''
    
    
    #cursor.execute(table)

    ## These commands work!!

    #insert_script = '''INSERT INTO PEOPLE (ID, NAME, PASSWORD) VALUES (%s, %s, %s)'''

    #insert_value = (3, "lucas@gmail.com", "turbo")

    #cursor.execute(insert_script, insert_value)









    #list_tables()

    insert_into_table("people", 2, "ness@gmail.com", "earthbound")

    #create_table("people", "id", "email", "password" )

    list_columns("people")

    #delete_table("people")

    #list_tables()

    

    

    connection.commit()










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
