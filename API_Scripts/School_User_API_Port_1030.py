from flask import Flask, request
import mysql.connector
import json
from datetime import date


app = Flask(__name__)

@app.route('/HLGD_HL3_Users')

def MySQL_User_Table():

    # Obtaining Variables
    school_name = request.args.get('schoolname')
    user_id = request.args.get('userid')
    sdate = request.args.get('startdate')
    edate = request.args.get('enddate')

    if len(school_name) >= 1:
        school_name_pass = school_name
    else:
        school_name_pass = ""

    if len(user_id) >= 1:
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


    # MySQL Credentials
    mydb_HLGD = mysql.connector.connect(user='root', password = 'woogi20#', host= '127.0.0.1', port = 3306, database='HLGD')
    mycursor_HLGD = mydb_HLGD.cursor()

    # Estabilishing Which Query To Run and Return
    if user_id_pass == "0":
        if school_name_pass == "":
            #Run Original Query

            mycursor_HLGD.execute('''SELECT MAIN.User_ID, MAIN.User_Name, MAIN.School_Name, MAIN.`Most Recent Login`, MAIN.`Total Number Of Logins`, MAIN.`Average Playtime Minutes Per Login`, MAIN.`Number Of Missions Completed`, MAIN.`Number Of Videos Watched`, MAIN.`Video Watch time (HH:MM:SS)` FROM (SELECT USR.User_ID, USR.User_Name, USR.School_ID, USR.School_Name,
                                IF(SES.`Latest Session` IS NULL, "", SES.`Latest Session`) as "Most Recent Login",
                                IF(SES.`Number Of Logins` IS NULL, "", SES.`Number Of Logins`) as "Total Number Of Logins",
                                IF(SES.`Average Session Length`IS NULL, "", SES.`Average Session Length`) as "Average Playtime Minutes Per Login",
                                IF(MIS.Complete_Missions IS NULL, "", MIS.Complete_Missions) AS "Number Of Missions Completed",
                                IF(VID.`Videos Watched` IS NULL, "", VID.`Videos Watched`) AS "Number Of Videos Watched",
                                IF(VID.`Video Watch Time` IS NULL, "", VID.`Video Watch Time`) as "Video Watch Time (HH:MM:SS)"
                                FROM HLGD.HL3_Users AS USR
                                LEFT JOIN (SELECT user_id, sum(1) as "Complete_Missions" FROM woogi0_1.`hlmissionactivity` WHERE activity = "GAME_END" AND c_time >= unix_timestamp("'''+sdate_pass+'''") and c_time <= unix_timestamp("'''+edate_pass+'''") GROUP BY user_id) AS MIS ON USR.User_ID = MIS.user_id
                                LEFT JOIN (SELECT user_id, max(Date) as "Latest Session", round(avg(Minutes), 0) as "Average Session Length", count(Date) as "Number Of Logins" FROM (SELECT SessionData.user_id, SessionData.session_id, SessionData.Date, SessionData.Minutes FROM (SELECT  user_id, session_id, left(from_unixtime(time), 10) as "Date", ROUND(sum(online)/60) as "Minutes" FROM woogi0_1.`wcreateusereventlog` WHERE app_name = 'hl3.0'AND time >= UNIX_TIMESTAMP("'''+sdate_pass+'''") AND time <= UNIX_TIMESTAMP("'''+edate_pass+'''") GROUP BY `user_id`, session_id) as SessionData LEFT JOIN (SELECT * FROM HLGD.HL3_Users) as UserData on SessionData.user_id = UserData.User_ID WHERE UserData.School_ID != "0" AND UserData.School_ID != "2" AND UserData.User_Name != "mbutcher" AND UserData.User_Name != "Mrcoyan" AND UserData.User_Name != "mrssalmons" AND UserData.User_Name != "mrspanda") as TM GROUP BY user_id) AS SES ON USR.User_ID = SES.user_id
                                LEFT JOIN (SELECT TM.user_id, TM.`Videos Watched`, TM.duration, concat(TM.Hour, ":", TM.Minutes,":",TM.Secs) as "Video Watch Time" FROM (SELECT *, if(length(floor(duration/60/60))=1, concat("0", floor(duration/60/60)), floor(duration/60/60)) as "Hour", if(length(floor(((duration/60/60)-floor(duration/60/60))*60))=1,concat("0",floor(((duration/60/60)-floor(duration/60/60))*60)),floor(((duration/60/60)-floor(duration/60/60))*60)) as Minutes,
                                if(length(round(((((duration/60/60)-floor(duration/60/60))*60)-floor(((duration/60/60)-floor(duration/60/60))*60))*60, 0))=1, concat("0",round(((((duration/60/60)-floor(duration/60/60))*60)-floor(((duration/60/60)-floor(duration/60/60))*60))*60, 0)), round(((((duration/60/60)-floor(duration/60/60))*60)-floor(((duration/60/60)-floor(duration/60/60))*60))*60, 0)) as "Secs"
                                FROM (SELECT user_id, sum(duration) as "duration", count(video_id) as "Videos Watched" FROM woogi0_1.wcreatevideolog WHERE `event` = 0 AND `time` >= UNIX_TIMESTAMP("'''+sdate_pass+'''") AND `time` <= UNIX_TIMESTAMP("'''+edate_pass+'''") GROUP BY user_id) as TM) as TM) AS VID ON USR.User_ID = VID.user_id
                                WHERE USR.School_ID != "0" AND
                                USR.School_ID != "2" and
                                USR.User_Name != "beccadowecca" and
                                USR.User_Name != "coachbecca" and
                                USR.User_Name != "realscottdow3" and
                                USR.User_Name != "scottdow3" and
                                USR.User_Name != "jcabello22823-2" and
                                USR.User_Name != "testjoe13023" and
                                USR.User_Name != "wtest800" and
                                USR.User_Name != "waltertestschool001" and
                                USR.User_Name != "walterschooltest002" and
                                USR.User_Name != "jtest3723" and
                                USR.User_Name != "jacksontest1" and
                                USR.User_Name != "jacksontest" and
                                USR.User_Name != "kindratest032123" and
                                USR.User_Name != "jontest321231") AS MAIN
                                WHERE MAIN.`Most Recent Login` != "";''')
            result = mycursor_HLGD.fetchall()

        else:
            # Run Query With School_Name Modifier

            mycursor_HLGD.execute('''SELECT MAIN.User_ID, MAIN.User_Name, MAIN.School_Name, MAIN.`Most Recent Login`, MAIN.`Total Number Of Logins`, MAIN.`Average Playtime Minutes Per Login`, MAIN.`Number Of Missions Completed`, MAIN.`Number Of Videos Watched`, MAIN.`Video Watch time (HH:MM:SS)` FROM (SELECT USR.User_ID, USR.User_Name, USR.School_ID, USR.School_Name,
                                IF(SES.`Latest Session` IS NULL, "", SES.`Latest Session`) as "Most Recent Login",
                                IF(SES.`Number Of Logins` IS NULL, "", SES.`Number Of Logins`) as "Total Number Of Logins",
                                IF(SES.`Average Session Length`IS NULL, "", SES.`Average Session Length`) as "Average Playtime Minutes Per Login",
                                IF(MIS.Complete_Missions IS NULL, "", MIS.Complete_Missions) AS "Number Of Missions Completed",
                                IF(VID.`Videos Watched` IS NULL, "", VID.`Videos Watched`) AS "Number Of Videos Watched",
                                IF(VID.`Video Watch Time` IS NULL, "", VID.`Video Watch Time`) as "Video Watch Time (HH:MM:SS)"
                                FROM HLGD.HL3_Users AS USR
                                LEFT JOIN (SELECT user_id, sum(1) as "Complete_Missions" FROM woogi0_1.`hlmissionactivity` WHERE activity = "GAME_END" AND c_time >= unix_timestamp("'''+sdate_pass+'''") and c_time <= unix_timestamp("'''+edate_pass+'''") GROUP BY user_id) AS MIS ON USR.User_ID = MIS.user_id
                                LEFT JOIN (SELECT user_id, max(Date) as "Latest Session", round(avg(Minutes), 0) as "Average Session Length", count(Date) as "Number Of Logins" FROM (SELECT SessionData.user_id, SessionData.session_id, SessionData.Date, SessionData.Minutes FROM (SELECT  user_id, session_id, left(from_unixtime(time), 10) as "Date", ROUND(sum(online)/60) as "Minutes" FROM woogi0_1.`wcreateusereventlog` WHERE app_name = 'hl3.0'AND time >= UNIX_TIMESTAMP("'''+sdate_pass+'''") AND time <= UNIX_TIMESTAMP("'''+edate_pass+'''") GROUP BY `user_id`, session_id) as SessionData LEFT JOIN (SELECT * FROM HLGD.HL3_Users) as UserData on SessionData.user_id = UserData.User_ID WHERE UserData.School_ID != "0" AND UserData.School_ID != "2" AND UserData.User_Name != "mbutcher" AND UserData.User_Name != "Mrcoyan" AND UserData.User_Name != "mrssalmons" AND UserData.User_Name != "mrspanda") as TM GROUP BY user_id) AS SES ON USR.User_ID = SES.user_id
                                LEFT JOIN (SELECT TM.user_id, TM.`Videos Watched`, TM.duration, concat(TM.Hour, ":", TM.Minutes,":",TM.Secs) as "Video Watch Time" FROM (SELECT *, if(length(floor(duration/60/60))=1, concat("0", floor(duration/60/60)), floor(duration/60/60)) as "Hour", if(length(floor(((duration/60/60)-floor(duration/60/60))*60))=1,concat("0",floor(((duration/60/60)-floor(duration/60/60))*60)),floor(((duration/60/60)-floor(duration/60/60))*60)) as Minutes,
                                if(length(round(((((duration/60/60)-floor(duration/60/60))*60)-floor(((duration/60/60)-floor(duration/60/60))*60))*60, 0))=1, concat("0",round(((((duration/60/60)-floor(duration/60/60))*60)-floor(((duration/60/60)-floor(duration/60/60))*60))*60, 0)), round(((((duration/60/60)-floor(duration/60/60))*60)-floor(((duration/60/60)-floor(duration/60/60))*60))*60, 0)) as "Secs"
                                FROM (SELECT user_id, sum(duration) as "duration", count(video_id) as "Videos Watched" FROM woogi0_1.wcreatevideolog WHERE `event` = 0 AND `time` >= UNIX_TIMESTAMP("'''+sdate_pass+'''") AND `time` <= UNIX_TIMESTAMP("'''+edate_pass+'''") GROUP BY user_id) as TM) as TM) AS VID ON USR.User_ID = VID.user_id
                                WHERE USR.School_ID != "0" AND
                                USR.School_ID != "2" and
                                USR.User_Name != "beccadowecca" and
                                USR.User_Name != "coachbecca" and
                                USR.User_Name != "realscottdow3" and
                                USR.User_Name != "scottdow3" and
                                USR.User_Name != "jcabello22823-2" and
                                USR.User_Name != "testjoe13023" and
                                USR.User_Name != "wtest800" and
                                USR.User_Name != "waltertestschool001" and
                                USR.User_Name != "walterschooltest002" and
                                USR.User_Name != "jtest3723" and
                                USR.User_Name != "jacksontest1" and
                                USR.User_Name != "jacksontest" and
                                USR.User_Name != "kindratest032123" and
                                USR.User_Name != "jontest321231") AS MAIN
                                WHERE MAIN.`Most Recent Login` != "" AND MAIN.School_Name = "'''+school_name_pass+'''";''')
            result = mycursor_HLGD.fetchall()
    else:
        # Run Query With User_name Filter

        mycursor_HLGD.execute('''SELECT MAIN.User_ID, MAIN.User_Name, MAIN.School_Name, MAIN.`Most Recent Login`, MAIN.`Total Number Of Logins`, MAIN.`Average Playtime Minutes Per Login`, MAIN.`Number Of Missions Completed`, MAIN.`Number Of Videos Watched`, MAIN.`Video Watch time (HH:MM:SS)` FROM (SELECT USR.User_ID, USR.User_Name, USR.School_ID, USR.School_Name,
                                IF(SES.`Latest Session` IS NULL, "", SES.`Latest Session`) as "Most Recent Login",
                                IF(SES.`Number Of Logins` IS NULL, "", SES.`Number Of Logins`) as "Total Number Of Logins",
                                IF(SES.`Average Session Length`IS NULL, "", SES.`Average Session Length`) as "Average Playtime Minutes Per Login",
                                IF(MIS.Complete_Missions IS NULL, "", MIS.Complete_Missions) AS "Number Of Missions Completed",
                                IF(VID.`Videos Watched` IS NULL, "", VID.`Videos Watched`) AS "Number Of Videos Watched",
                                IF(VID.`Video Watch Time` IS NULL, "", VID.`Video Watch Time`) as "Video Watch Time (HH:MM:SS)"
                                FROM HLGD.HL3_Users AS USR
                                LEFT JOIN (SELECT user_id, sum(1) as "Complete_Missions" FROM woogi0_1.`hlmissionactivity` WHERE activity = "GAME_END" AND c_time >= unix_timestamp("'''+sdate_pass+'''") and c_time <= unix_timestamp("'''+edate_pass+'''") GROUP BY user_id) AS MIS ON USR.User_ID = MIS.user_id
                                LEFT JOIN (SELECT user_id, max(Date) as "Latest Session", round(avg(Minutes), 0) as "Average Session Length", count(Date) as "Number Of Logins" FROM (SELECT SessionData.user_id, SessionData.session_id, SessionData.Date, SessionData.Minutes FROM (SELECT  user_id, session_id, left(from_unixtime(time), 10) as "Date", ROUND(sum(online)/60) as "Minutes" FROM woogi0_1.`wcreateusereventlog` WHERE app_name = 'hl3.0'AND time >= UNIX_TIMESTAMP("'''+sdate_pass+'''") AND time <= UNIX_TIMESTAMP("'''+edate_pass+'''") GROUP BY `user_id`, session_id) as SessionData LEFT JOIN (SELECT * FROM HLGD.HL3_Users) as UserData on SessionData.user_id = UserData.User_ID WHERE UserData.School_ID != "0" AND UserData.School_ID != "2" AND UserData.User_Name != "mbutcher" AND UserData.User_Name != "Mrcoyan" AND UserData.User_Name != "mrssalmons" AND UserData.User_Name != "mrspanda") as TM GROUP BY user_id) AS SES ON USR.User_ID = SES.user_id
                                LEFT JOIN (SELECT TM.user_id, TM.`Videos Watched`, TM.duration, concat(TM.Hour, ":", TM.Minutes,":",TM.Secs) as "Video Watch Time" FROM (SELECT *, if(length(floor(duration/60/60))=1, concat("0", floor(duration/60/60)), floor(duration/60/60)) as "Hour", if(length(floor(((duration/60/60)-floor(duration/60/60))*60))=1,concat("0",floor(((duration/60/60)-floor(duration/60/60))*60)),floor(((duration/60/60)-floor(duration/60/60))*60)) as Minutes,
                                if(length(round(((((duration/60/60)-floor(duration/60/60))*60)-floor(((duration/60/60)-floor(duration/60/60))*60))*60, 0))=1, concat("0",round(((((duration/60/60)-floor(duration/60/60))*60)-floor(((duration/60/60)-floor(duration/60/60))*60))*60, 0)), round(((((duration/60/60)-floor(duration/60/60))*60)-floor(((duration/60/60)-floor(duration/60/60))*60))*60, 0)) as "Secs"
                                FROM (SELECT user_id, sum(duration) as "duration", count(video_id) as "Videos Watched" FROM woogi0_1.wcreatevideolog WHERE `event` = 0 AND `time` >= UNIX_TIMESTAMP("'''+sdate_pass+'''") AND `time` <= UNIX_TIMESTAMP("'''+edate_pass+'''") GROUP BY user_id) as TM) as TM) AS VID ON USR.User_ID = VID.user_id
                                WHERE USR.School_ID != "0" AND
                                USR.School_ID != "2" and
                                USR.User_Name != "beccadowecca" and
                                USR.User_Name != "coachbecca" and
                                USR.User_Name != "realscottdow3" and
                                USR.User_Name != "scottdow3" and
                                USR.User_Name != "jcabello22823-2" and
                                USR.User_Name != "testjoe13023" and
                                USR.User_Name != "wtest800" and
                                USR.User_Name != "waltertestschool001" and
                                USR.User_Name != "walterschooltest002" and
                                USR.User_Name != "jtest3723" and
                                USR.User_Name != "jacksontest1" and
                                USR.User_Name != "jacksontest" and
                                USR.User_Name != "kindratest032123" and
                                USR.User_Name != "jontest321231") AS MAIN
                                WHERE MAIN.`Most Recent Login` != "" AND MAIN.User_ID = "'''+user_id_pass+'''";''')
        result = mycursor_HLGD.fetchall()

    return json.dumps(result)

app.run(host = "0.0.0.0", port="1030")





