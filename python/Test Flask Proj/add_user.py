import os
import psycopg2


def main():
    
    connection = psycopg2.connect(
    host="free-tier11.gcp-us-east1.cockroachlabs.cloud",
    port=26257, 
    dbname="terra-hamster-556.defaultdb",
    user="dev_link", 
    password="7sHSHqWHzdQJUrFrFclaSg")

    cursor = connection.cursor()

    ##example
    #create_table("test", "ID", "email", "password")


    def insert_into_table(table_name, primary_id, column_1, column_2):
        insert_script = '''INSERT INTO {table} (id, email, password) VALUES (%s, %s, %s)'''.format(table=table_name)
        insert_value = (primary_id, column_1, column_2)
        cursor.execute(insert_script, insert_value)
        connection.commit()
        print("Data inserted successfully: {p}, {c1}, {c2}".format(p = primary_id, c1 = column_1, c2 = column_2))



    ## Current Management Functions ##


    #insert_into_table("people", 5, "opal@gmail.com", "goldnsilver")



    
    
    #Closing the connection
    connection.close()

   


if __name__ == "__main__":
    main()
