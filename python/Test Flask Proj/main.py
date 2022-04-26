from flask import Flask, request
from flask_cors import CORS, cross_origin
import psycopg2

app = Flask(__name__)

cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'


connection = psycopg2.connect(
host="free-tier11.gcp-us-east1.cockroachlabs.cloud",
port=26257, 
dbname="terra-hamster-556.defaultdb",
user="dev_link", 
password="7sHSHqWHzdQJUrFrFclaSg")

cursor = connection.cursor()

@app.route("/", methods=['GET', 'POST', 'OPTIONS'])
@cross_origin()



def index():

    def insert_into_table(table_name, primary_id, column_1, column_2):
        insert_script = '''INSERT INTO {table} (id, email, password) VALUES (%s, %s, %s)'''.format(table=table_name)
        insert_value = (primary_id, column_1, column_2)
        cursor.execute(insert_script, insert_value)
        connection.commit()
        print("Data inserted successfully: {p}, {c1}, {c2}".format(p = primary_id, c1 = column_1, c2 = column_2))

    def get_new_id():
        cursor.execute('''SELECT max(ID) FROM people''')
        id = cursor.fetchone()
        num = 0
        for interger in id:
            num = interger
        return num + 1

    
    #return "<h1>Hello!</h1>"

    #data = request.data  # raw data
    data = request.json # json (if content-type of application/json is sent with the request)
    #print(request.get_json(force=True))  # json (if content-type of application/json is not sent)
    if request.method=='GET':
        #return'<h1>Running</h1> <meta http-equiv="refresh" content="2"> <h2>{{data}}</h2> '
        return'<h1>Running GET</h1>'
    elif request.method=='POST':
        #new_data = data.split(":")
        #print(data)
        username = data["userName"]
        password = data["password"]
        insert_into_table("people", get_new_id(), username, password)
        
        #print(username, password)
        return'<h1>Running POST</h1>'
        
    else:
        #print(data)
        
        return'<h1>Running ELSE</h1>'

