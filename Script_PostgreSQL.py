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

    def create_table(name, email, password):
        table = '''CREATE TABLE {}({} VARCHAR(20) NOT NULL,{} VARCHAR(20))'''.format(name, email, password)
        cursor.execute(table)
        print("Table {} Created".format(name))
        connection.commit()


    create_table("Test1", "nancy@gmail.com", )

    
    
    #cursor.execute("DROP TABLE IF EXISTS USERS")

    #statements = '''CREATE TABLE USERS(
    #EMAIL VARCHAR(20) NOT NULL,
    #PASSWORD VARCHAR(20))'''


    #statements = '''CREATE TABLE USERS(
    #FIRST_NAME CHAR(20) NOT NULL,
    #LAST_NAME CHAR(20),
    #AGE INT,
    #SEX CHAR(1),
    #INCOME FLOAT
    #)'''

    #cursor.execute(statements)

    #print("Table created successfully........")
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
