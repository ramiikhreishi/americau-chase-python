import mysql.connector
import pandas as pd

mydb_woogi0_1 = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='woogi0_1')

mydb_HLGD = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='HLGD')

mycursor_HLGD = mydb_HLGD.cursor()

try:
    mycursor_HLGD.execute('''CREATE TABLE HLGD.Dash_Missions (SELECT T1.user_id, T1.User_Name, T1.School_Name, T1.scene_id, T2.theme_name, T2.title_name, T1.`Date/Time`, T1.`Status` FROM HLGD.HL3_Mission_Table as T1 LEFT JOIN (select scene_id, theme_name, title_name from woogi0_1.`wcskbooknpclines`) as T2 on T1.scene_id = T2.scene_id WHERE T2.title_name IS NOT NULL AND T2.title_name NOT LIKE "%test%" and T1.User_Name NOT LIKE "%test%");''')

except:
    mycursor_HLGD.execute('DROP Table HLGD.Dash_Missions;')
    mycursor_HLGD.execute('''CREATE TABLE HLGD.Dash_Missions (SELECT T1.user_id, T1.User_Name, T1.School_Name, T1.scene_id, T2.theme_name, T2.title_name, T1.`Date/Time`, T1.`Status` FROM HLGD.HL3_Mission_Table as T1 LEFT JOIN (select scene_id, theme_name, title_name from woogi0_1.`wcskbooknpclines`) as T2 on T1.scene_id = T2.scene_id WHERE T2.title_name IS NOT NULL AND T2.title_name NOT LIKE "%test%" and T1.User_Name NOT LIKE "%test%");''')
    

mydb_HLGD.close()
