from flask import Flask, request
import mysql.connector
import json
import pandas as pd
from datetime import date


app = Flask(__name__)


@app.route('/HLGD_HL3_Skill_Points')
def MySQL_User_Table(): 

    # Obtaining Variables

    school_name = request.args.get('schoolname')
    sdate = request.args.get('startdate')
    edate = request.args.get('enddate')

    if len(school_name) >= 1:
        school_name_pass = school_name
        print(school_name)
    else:
        school_name_pass = ""
        print(school_name_pass,'1')

    if len(sdate) >= 1:
        sdate_pass = sdate
        print(sdate)
    else:
        sdate_pass = "2022-12-01"

    if len(edate) >= 1:
        edate_pass = edate
        print(edate)
    else:
        edate_pass = date.today()

    # MySQL Credentials

    mydb_HLGD = mysql.connector.connect(
        user='root', password='woogi20#', host='127.0.0.1', port=3306, database='HLGD')
    mycursor_HLGD = mydb_HLGD.cursor()

  # Estabilishing Which Query To Run and Return
    if school_name_pass == "":
        query  = '''SELECT sum(T1.`T20 SK 1 - Social & Emotional Learning - Points`) as `Social & Emotional Learning`,
                                sum(T1.`T20 SK 2 - Character - Points`) as `Character`,
                                sum(T1.`T20 SK 3 - Creativity - Points`) as `Creativity`,
                                sum(T1.`T20 SK 4 - Lifelong Learner - Points`) as `Lifelong Learner`,
                                sum(T1.`T20 SK 5 - Health & Wellness - Points`) as `Health & Wellness`,
                                sum(T1.`T20 SK 6 - Resilience - Points`) as `Resilience`,
                                sum(T1.`T20 SK 7 - Distraction Management - Points`) as `Distraction Management`,
                                sum(T1.`T20 SK 8 - Technology Hardware & Coding - Points`) as `Technology Hardware & Coding`,
                                sum(T1.`T20 SK 9 - Trades Skills - Points`) as `Trades Skills`,
                                sum(T1.`T20 SK 10 - Cultural Understanding - Points`) as `Cultural Understanding`,
                                sum(T1.`T20 SK 11 - Civics Literacy - Points`) as `Civics Literacy`,
                                sum(T1.`T20 SK 12 - Environmental Literacy - Points`) as `Environmental Literacy`,
                                sum(T1.`T20 SK 13 - Communication - Points`) as `Communication`,
                                sum(T1.`T20 SK 14 - Teamwork - Points`) as `Teamwork`,
                                sum(T1.`T20 SK 15 - Leadership - Points`) as `Leadership`,
                                sum(T1.`T20 SK 16 - Digitial & Information Literacy - Points`) as `Digitial & Information Literacy`,
                                sum(T1.`T20 SK 17 - Entrepreneurship - Points`) as `Entrepreneurship`,
                                sum(T1.`T20 SK 18 - Problem Solving - Points`) as `Problem Solving`,
                                sum(T1.`T20 SK 19 - Financial Literacy - Points`) as `Financial Literacy`,
                                sum(T1.`T20 SK 20 - Habit & Goal Setting - Points`) as `Habit & Goal Setting`
                                FROM HLGD.HL3_Mission_Skills_Data AS T1
                                JOIN HLGD.HL3_Users AS T2 ON T1.user_id = T2.user_id
                                WHERE T2.school_name != "Freedom University" AND T1.Date >="'''+sdate_pass+'''" AND T1.Date <= "'''+edate_pass+'''"
                                ;'''
        mycursor_HLGD.execute(query)
        result = mycursor_HLGD.fetchall()
        columns = mycursor_HLGD.column_names


    else:
        query = '''SELECT sum(T1.`T20 SK 1 - Social & Emotional Learning - Points`) as `Social & Emotional Learning`,
                                sum(T1.`T20 SK 2 - Character - Points`) as `Character`,
                                sum(T1.`T20 SK 3 - Creativity - Points`) as `Creativity`,
                                sum(T1.`T20 SK 4 - Lifelong Learner - Points`) as `Lifelong Learner`,
                                sum(T1.`T20 SK 5 - Health & Wellness - Points`) as `Health & Wellness`,
                                sum(T1.`T20 SK 6 - Resilience - Points`) as `Resilience`,
                                sum(T1.`T20 SK 7 - Distraction Management - Points`) as `Distraction Management,
                                sum(T1.`T20 SK 8 - Technology Hardware & Coding - Points`) as `Technology Hardware & Coding`,
                                sum(T1.`T20 SK 9 - Trades Skills - Points`) as `Trades Skills`,
                                sum(T1.`T20 SK 10 - Cultural Understanding - Points`) as `Cultural UnderstandingT20 SK10`,
                                sum(T1.`T20 SK 11 - Civics Literacy - Points`) as `Civics Literacy`,
                                sum(T1.`T20 SK 12 - Environmental Literacy - Points`) as `Environmental Literacy`,
                                sum(T1.`T20 SK 13 - Communication - Points`) as `Communication`,
                                sum(T1.`T20 SK 14 - Teamwork - Points`) as `Teamwork`,
                                sum(T1.`T20 SK 15 - Leadership - Points`) as `Leadership`,
                                sum(T1.`T20 SK 16 - Digitial & Information Literacy - Points`) as `Digitial & Information Literacy`,
                                sum(T1.`T20 SK 17 - Entrepreneurship - Points`) as `Entrepreneurship`,
                                sum(T1.`T20 SK 18 - Problem Solving - Points`) as `Problem Solving`,
                                sum(T1.`T20 SK 19 - Financial Literacy - Points`) as `Financial Literacy`,
                                sum(T1.`T20 SK 20 - Habit & Goal Setting - Points`) as `Habit & Goal Setting`
                                FROM HLGD.HL3_Mission_Skills_Data AS T1
                                JOIN HLGD.HL3_Users AS T2 ON T1.user_id = T2.user_id
                                WHERE T2.school_name != "Freedom University" AND T2.school_name = "'''+school_name_pass+'''" AND T1.Date >="'''+sdate_pass+'''" AND T1.Date <="'''+edate_pass+'''";'''
        mycursor_HLGD.execute(query)
        result = mycursor_HLGD.fetchall()
        columns = mycursor_HLGD.column_names

    return json.dumps(result)


app.run(host="0.0.0.0", port="1040")



