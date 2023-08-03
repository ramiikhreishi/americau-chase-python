import mysql.connector
import pandas as pd

mydb_woogi0_1 = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='woogi0_1')

mydb_HLGD = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='HLGD')

mycursor_woogi0_1 = mydb_woogi0_1.cursor()

mycursor_HLGD = mydb_HLGD.cursor()


try:
    mycursor_HLGD.execute("""create table HLGD.HL3_Mission_Table (SELECT STR.user_id, STR.User_Name, STR.School_Name, STR.`Date/Time`, STR.scene_id, if(FIN.Status IS NULL, STR.Status, FIN.Status) as "Status" FROM (SELECT T1.user_id, T2.User_Name, T2.School_Name, left(from_unixtime(c_time), 10) as "Date/Time", T1.scene_id, "Started" as "Status" FROM (Select * FROM woogi0_1.`hlmissionactivity` WHERE activity LIKE "%start%")  as T1
                                LEFT JOIN (SELECT * FROM HLGD.HL3_Complete_User_List) as T2 on T1.user_id = T2.User_ID
                                WHERE T2.School_Name IS NOT NULL  AND
                                T2.School_Name != "Developer Testing" AND
                                T2.School_Name != "Freedom University" AND
                                T2.User_Name NOT LIKE "%scottdow%" AND
                                T1.user_id != "64" AND
                                T2.User_Name NOT LIKE "%jportik%" AND
                                T2.User_Name NOT LIKE "%mbutcher%" AND
                                T2.User_Name NOT LIKE "%caiyuan07281%"
                                GROUP BY T1.user_id, T2.User_Name, T1.scene_id, T2.School_Name, left(from_unixtime(c_time), 10)) as STR
                                LEFT JOIN (SELECT T1.user_id, left(from_unixtime(c_time), 10) as "Date/Time", T1.scene_id, "Finished" as "Status" FROM(Select * FROM woogi0_1.`hlmissionactivity` WHERE activity LIKE "%end%") as T1
                                LEFT JOIN (SELECT * FROM HLGD.HL3_Complete_User_List) as T2 on T1.user_id = T2.User_ID
                                WHERE T2.School_Name IS NOT NULL AND
                                T1.activity = "GAME_END" AND
                                T2.School_Name != "Developer Testing" AND
                                T2.School_Name != "Freedom University" AND
                                T2.User_Name NOT LIKE "%scottdow%" AND
                                T1.user_id != "64" AND
                                T2.User_Name NOT LIKE "%jportik%" AND
                                T2.User_Name NOT LIKE "%mbutcher%" AND
                                T2.User_Name NOT LIKE "%caiyuan07281%"
                                GROUP BY T1.user_id, T2.User_Name, T1.scene_id, T2.School_Name, left(from_unixtime(c_time), 10)) as FIN ON STR.user_id = FIN.user_id AND STR.`Date/Time` = FIN.`Date/Time` AND STR.scene_id = FIN.scene_id);""")
except:
    mycursor_HLGD.execute('DROP Table HLGD.HL3_Mission_Table;')
    mycursor_HLGD.execute('''create table HLGD.HL3_Mission_Table (SELECT STR.user_id, STR.User_Name, STR.School_Name, STR.`Date/Time`, STR.scene_id, if(FIN.Status IS NULL, STR.Status, FIN.Status) as "Status" FROM (SELECT T1.user_id, T2.User_Name, T2.School_Name, left(from_unixtime(c_time), 10) as "Date/Time", T1.scene_id, "Started" as "Status" FROM (Select * FROM woogi0_1.`hlmissionactivity` WHERE activity LIKE "%start%")  as T1
                                LEFT JOIN (SELECT * FROM HLGD.HL3_Complete_User_List) as T2 on T1.user_id = T2.User_ID
                                WHERE T2.School_Name IS NOT NULL  AND
                                T2.School_Name != "Developer Testing" AND
                                T2.School_Name != "Freedom University" AND
                                T2.User_Name NOT LIKE "%scottdow%" AND
                                T1.user_id != "64" AND
                                T2.User_Name NOT LIKE "%jportik%" AND
                                T2.User_Name NOT LIKE "%mbutcher%" AND
                                T2.User_Name NOT LIKE "%caiyuan07281%"
                                GROUP BY T1.user_id, T2.User_Name, T1.scene_id, T2.School_Name, left(from_unixtime(c_time), 10)) as STR
                                LEFT JOIN (SELECT T1.user_id, left(from_unixtime(c_time), 10) as "Date/Time", T1.scene_id, "Finished" as "Status" FROM(Select * FROM woogi0_1.`hlmissionactivity` WHERE activity LIKE "%end%") as T1
                                LEFT JOIN (SELECT * FROM HLGD.HL3_Complete_User_List) as T2 on T1.user_id = T2.User_ID
                                WHERE T2.School_Name IS NOT NULL AND
                                T1.activity = "GAME_END" AND
                                T2.School_Name != "Developer Testing" AND
                                T2.School_Name != "Freedom University" AND
                                T2.User_Name NOT LIKE "%scottdow%" AND
                                T1.user_id != "64" AND
                                T2.User_Name NOT LIKE "%jportik%" AND
                                T2.User_Name NOT LIKE "%mbutcher%" AND
                                T2.User_Name NOT LIKE "%caiyuan07281%"
                                GROUP BY T1.user_id, T2.User_Name, T1.scene_id, T2.School_Name, left(from_unixtime(c_time), 10)) as FIN ON STR.user_id = FIN.user_id AND STR.`Date/Time` = FIN.`Date/Time` AND STR.scene_id = FIN.scene_id);''')


mydb_HLGD.close()

mydb_woogi0_1.close()

