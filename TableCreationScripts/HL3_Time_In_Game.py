import mysql.connector
import pandas as pd

mydb_woogi0_1 = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='woogi0_1')

mydb_HLGD = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='HLGD')

mycursor_HLGD = mydb_HLGD.cursor()

try:
    mycursor_HLGD.execute('''Create TABLE HLGD.HL3_Time_In_Game (SELECT SessionData.user_id, UserData.User_Name, UserData.School_Name, UserData.School_ID, SessionData.session_id, SessionData.Date, SessionData.Minutes
                                FROM (SELECT  user_id, session_id, left(from_unixtime(time), 10) as "Date", ROUND(sum(online)/60) as "Minutes" FROM woogi0_1.`wcreateusereventlog` WHERE app_name = 'hl3.0'AND time > UNIX_TIMESTAMP('2022-12-01 00:00:00') GROUP BY `user_id`, session_id) as SessionData
                                LEFT JOIN (SELECT * FROM HLGD.HL3_Complete_User_List) as UserData on SessionData.user_id = UserData.User_ID
                                WHERE UserData.School_ID != "0" AND UserData.School_ID != "2" AND UserData.User_Name != "mbutcher" AND UserData.User_Name != "Mrcoyan" AND UserData.User_Name != "mrssalmons" AND UserData.User_Name != "mrspanda" );''')
except:
    mycursor_HLGD.execute('DROP Table HLGD.HL3_Time_In_Game;')
    mycursor_HLGD.execute('''Create TABLE HLGD.HL3_Time_In_Game (SELECT SessionData.user_id, UserData.User_Name, UserData.School_Name, UserData.School_ID, SessionData.session_id, SessionData.Date, SessionData.Minutes
                                FROM (SELECT  user_id, session_id, left(from_unixtime(time), 10) as "Date", ROUND(sum(online)/60) as "Minutes" FROM woogi0_1.`wcreateusereventlog` WHERE app_name = 'hl3.0'AND time > UNIX_TIMESTAMP('2022-12-01 00:00:00') GROUP BY `user_id`, session_id) as SessionData
                                LEFT JOIN (SELECT * FROM HLGD.HL3_Complete_User_List) as UserData on SessionData.user_id = UserData.User_ID
                                WHERE UserData.School_ID != "0" AND UserData.School_ID != "2" AND UserData.User_Name != "mbutcher" AND UserData.User_Name != "Mrcoyan" AND UserData.User_Name != "mrssalmons" AND UserData.User_Name != "mrspanda" );''')


mydb_HLGD.close()
