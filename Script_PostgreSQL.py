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
    connection = psycopg2.connect(host="free-tier11.gcp-us-east1.cockroachlabs.cloud", port=26257, dbname="terra-hamster-556.defaultdb", user="dev_link", password="7sHSHqWHzdQJUrFrFclaSg")

    cursor = connection.cursor()
    
    #cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

    #statements = '''CREATE TABLE EMPLOYEE(
    #FIRST_NAME CHAR(20) NOT NULL,
    #LAST_NAME CHAR(20),
    #AGE INT,
    #SEX CHAR(1),
    #INCOME FLOAT
    #)'''

    #cursor.execute(statements)

    #print("Table created successfully........")
    #connection.commit()

    #cursor.execute('''INSERT INTO EMPLOYEE(FIRST_NAME, LAST_NAME, AGE, SEX,
    #INCOME) VALUES ('John', 'Smith', 32, 'M', 30000)''')
    
    cursor.execute('''SELECT * from EMPLOYEE''')

    result = cursor.fetchall()

    for data in result:
        print(data)

    #Commit your changes in the database
    #connection.commit()
    
    #Closing the connection
    #connection.close()


if __name__ == "__main__":
    main()
