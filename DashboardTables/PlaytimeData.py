import mysql.connector
import pandas as pd

mydb_woogi0_1 = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='woogi0_1')

mydb_HLGD = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='HLGD')

mycursor_HLGD = mydb_HLGD.cursor()

try:
    mycursor_HLGD.execute('''CREATE TABLE HLGD.PlaytimeData (SELECT user_id, User_Name, School_Name, sum(Minutes) as "Minutes" FROM HLGD.HL3_Time_In_Game where session_id != "" AND Minutes < 120 AND Minutes != 0 and User_Name != "scottdow3"  and User_Name != "caiyuan07281" and User_Name != "jportik" GROUP BY user_id, User_Name, School_Name);''')

except:
    mycursor_HLGD.execute('DROP Table HLGD.PlaytimeData;')
    mycursor_HLGD.execute('''CREATE TABLE HLGD.PlaytimeData (SELECT user_id, User_Name, School_Name, sum(Minutes) as "Minutes" FROM HLGD.HL3_Time_In_Game where session_id != "" AND Minutes < 120 AND Minutes != 0 and User_Name != "scottdow3"  and User_Name != "caiyuan07281" and User_Name != "jportik" GROUP BY user_id, User_Name, School_Name);''')

    
mydb_HLGD.close()
