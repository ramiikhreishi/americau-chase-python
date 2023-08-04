from flask import Flask, request
import mysql.connector
import pandas as pd
from datetime import date


app = Flask(__name__)


@app.route('/HLGD_HL3_Activities_API')
def MySQL_User_Table():

    mydb_HLGD = mysql.connector.connect(
        user='root', password='woogi20#', host='127.0.0.1', port=3306, database='HLGD')

    school_name = request.args.get('schoolname')
    user_id = request.args.get('userid')
    sdate = request.args.get('startdate')
    edate = request.args.get('enddate')

    query1 = "SELECT * FROM HLGD.HL3_Activities_Upon_Login;"

    Activities_Upon_Login = pd.read_sql(query1, mydb_HLGD)

    Users_and_Dates = Activities_Upon_Login[["user_id", "Date/Time"]]

    Users_and_Dates['Date'] = Users_and_Dates['Date/Time'].astype(
        'str').str[:10]

    Users_and_Dates['Hour'] = Users_and_Dates['Date/Time'].astype(
        'str').str[11:13]

    Users_and_Dates_Sorting = Users_and_Dates[["user_id", "Date", "Hour"]].drop_duplicates(
        subset=None, keep='first', inplace=False, ignore_index=False).reset_index(drop=True)

    Activity_sorting = Activities_Upon_Login.sort_values(by='Date/Time')

    Activity_sorting["Date"] = Activity_sorting['Date/Time'].astype(
        'str').str[:10]

    Activity_sorting["Hour"] = Activity_sorting['Date/Time'].astype(
        'str').str[11:13]

    Master_File = pd.DataFrame(columns=["user_id", "user_name", "school_name", "school_id", "Date", "Activity_Type_1", "Activity_Type_2", "Activity_Type_3",
                               "Activity_Type_4", "Activity_Type_5", "Activity_Type_6", "Activity_Type_7", "Activity_Type_8", "Activity_Type_9", "Activity_Type_10"])

    for a in range(len(Users_and_Dates_Sorting)):
        F_user_id = Users_and_Dates_Sorting['user_id'][a]
        F_Date = Users_and_Dates_Sorting['Date'][a]
        F_Hour = Users_and_Dates_Sorting['Hour'][a]

        Temp_Frame = Activity_sorting[(Activity_sorting.user_id == F_user_id) & (Activity_sorting.Date == F_Date) & (
            Activity_sorting.Hour == F_Hour)].sort_values(by='Date/Time').reset_index(drop=True)

        try:
            Act_1 = Temp_Frame['Activity_Type'][0]
        except:
            Act_1 = "No Activity"

        try:
            Act_2 = Temp_Frame['Activity_Type'][1]
        except:
            Act_2 = "No Activity"

        try:
            Act_3 = Temp_Frame['Activity_Type'][2]
        except:
            Act_3 = "No Activity"

        try:
            Act_4 = Temp_Frame['Activity_Type'][3]
        except:
            Act_4 = "No Activity"

        try:
            Act_5 = Temp_Frame['Activity_Type'][4]
        except:
            Act_5 = "No Activity"

        try:
            Act_6 = Temp_Frame['Activity_Type'][5]
        except:
            Act_6 = "No Activity"

        try:
            Act_7 = Temp_Frame['Activity_Type'][6]
        except:
            Act_7 = "No Activity"

        try:
            Act_8 = Temp_Frame['Activity_Type'][7]
        except:
            Act_8 = "No Activity"

        try:
            Act_9 = Temp_Frame['Activity_Type'][8]
        except:
            Act_9 = "No Activity"

        try:
            Act_10 = Temp_Frame['Activity_Type'][9]
        except:
            Act_10 = "No Activity"

        Aglo = [F_user_id, Temp_Frame['user_name'][0], Temp_Frame['school_name'][0], Temp_Frame['school_id']
                [0], Temp_Frame['Date'][0], Act_1, Act_2, Act_3, Act_4, Act_5, Act_6, Act_7, Act_8, Act_9, Act_10]

        Master_File.loc[a, ] = Aglo

        
        if len(school_name) >= 1:
            school_name_pass = school_name
        else:
            school_name_pass = ""

        if len(str(user_id)) >= 1:
            user_id_pass = user_id
        else:
            user_id_pass = "0"

        if len(sdate) >= 1:
            sdate_pass = sdate
        else:
            sdate_pass = "2022-12-01"

        if len(edate) >= 1:
            edate_pass = edate
        else:
            edate_pass = str(date.today())

        if user_id_pass == "0":
            if school_name_pass == "":
                Final = Master_File[(Master_File.Date >= sdate_pass) & (
                    Master_File.Date <= edate_pass)]
            else:
                Final = Master_File[(Master_File.school_name == school_name_pass) & (
                    Master_File.Date >= sdate_pass) & (Master_File.Date <= edate_pass)]
        elif school_name_pass == "":
            Final = Master_File[(Master_File.user_id >= user_id_pass) & (
                Master_File.Date >= sdate_pass) & (Master_File.Date <= edate_pass)]
        else:
            Final = Master_File

        Activities = pd.DataFrame(Activity_sorting['Activity_Type'].drop_duplicates(
            keep='first', inplace=False).reset_index(drop=True))

        Activities.loc[len(Activities)] = "No Activity"

        Return = pd.DataFrame()

        for B in range(len(Activities)):
            Activity1_Count = len(
                Final[(Final['Activity_Type_1'] == Activities['Activity_Type'][B])])
            Activity2_Count = len(
                Final[(Final['Activity_Type_2'] == Activities['Activity_Type'][B])])
            Activity3_Count = len(
                Final[(Final['Activity_Type_3'] == Activities['Activity_Type'][B])])
            Activity4_Count = len(
                Final[(Final['Activity_Type_4'] == Activities['Activity_Type'][B])])
            Activity5_Count = len(
                Final[(Final['Activity_Type_5'] == Activities['Activity_Type'][B])])
            Activity6_Count = len(
                Final[(Final['Activity_Type_6'] == Activities['Activity_Type'][B])])
            Activity7_Count = len(
                Final[(Final['Activity_Type_7'] == Activities['Activity_Type'][B])])
            Activity8_Count = len(
                Final[(Final['Activity_Type_8'] == Activities['Activity_Type'][B])])
            Activity9_Count = len(
                Final[(Final['Activity_Type_9'] == Activities['Activity_Type'][B])])
            Activity10_Count = len(
                Final[(Final['Activity_Type_10'] == Activities['Activity_Type'][B])])

            Return[Activities['Activity_Type'][B]] = [Activity1_Count, Activity2_Count, Activity3_Count, Activity4_Count,
                                                    Activity5_Count, Activity6_Count, Activity7_Count, Activity8_Count, Activity9_Count, Activity10_Count]

        Return.index = ["Activity 1", "Activity 2", "Activity 3", "Activity 4", "Activity 5",
                        "Activity 6", "Activity 7", "Activity 8", "Activity 9", "Activity 10"]

    return Return.to_json()


app.run(host="0.0.0.0", port="1010")


