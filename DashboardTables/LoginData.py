import mysql.connector
import pandas as pd

mydb_woogi0_1 = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='woogi0_1')

mydb_HLGD = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='HLGD')

mycursor_HLGD = mydb_HLGD.cursor()

try:
    mycursor_HLGD.execute('''CREATE TABLE HLGD.LoginData (SELECT user_id, user_name, school_name, min(Date) as "Earliest Login", max(Date) as "Most Recent Login", count(Date) as "Number Of Logins" FROM HLGD.HL3_Unique_User_Logins group by user_id, user_name, school_name);''')

except:
    mycursor_HLGD.execute('DROP Table HLGD.LoginData;')
    mycursor_HLGD.execute('''CREATE TABLE HLGD.LoginData (SELECT user_id, user_name, school_name, min(Date) as "Earliest Login", max(Date) as "Most Recent Login", count(Date) as "Number Of Logins" FROM HLGD.HL3_Unique_User_Logins group by user_id, user_name, school_name);''')
    

mydb_HLGD.close()
