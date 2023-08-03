from flask import Flask, request
import mysql.connector
import json
import pandas as pd
from datetime import date


app = Flask(__name__)

@app.route('/HLGD_HL3_School_List')

def MySQL_User_Table():

    # MySQL Credentials
    mydb_HLGD = mysql.connector.connect(user='root', password = 'woogi20#', host= '127.0.0.1', port = 3306, database='HLGD')
    mycursor_HLGD = mydb_HLGD.cursor()

    mycursor_HLGD.execute('''SELECT * FROM HLGD.HL3_School_List''')
    result = mycursor_HLGD.fetchall()

    return json.dumps(result)

app.run(host = "0.0.0.0", port="1020")
