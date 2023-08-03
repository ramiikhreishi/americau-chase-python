from flask import Flask, request
import mysql.connector
import json
import pandas as pd
from datetime import date

app = Flask(__name__)

@app.route('/HLGD_HL3_Unique_Logins')
def MySQL_User_Table():

    # Obtaining Variables
    school_name = request.args.get('schoolname')
    sdate = request.args.get('startdate')
    edate = request.args.get('enddate')

    if len(school_name) >= 1:
        school_name_pass = school_name
    else:
        school_name_pass = ""

    if len(sdate) >= 1:
        sdate_pass = sdate
    else:
        sdate_pass = "2022-12-01"


    if len(edate) >= 1:
        edate_pass = edate
    else:
        edate_pass = str(date.today())

    # MySQL Credentials
    mydb_HLGD = mysql.connector.connect(user='root', password = 'woogi20#', host= '127.0.0.1', port = 3306, database='HLGD')
    mycursor_HLGD = mydb_HLGD.cursor()

    # Estabilishing Which Query To Run and Return
    if school_name_pass == "":
        mycursor_HLGD.execute('SELECT Date, count(user_id) as " Unique Users" FROM HLGD.HL3_Unique_User_Logins WHERE Date >= "'+sdate_pass+'" AND Date <= "'+edate_pass+'" group by Date;')
        result = mycursor_HLGD.fetchall()

    else:
        mycursor_HLGD.execute('SELECT Date, count(user_id) as " Unique Users" FROM HLGD.HL3_Unique_User_Logins WHERE school_name Like "%'+school_name_pass+'%" AND Date >= "'+sdate_pass+'" AND Date <= "'+edate_pass+'" group by Date;')
        result = mycursor_HLGD.fetchall()

    return result

app.run(host="0.0.0.0", port = "1060")

