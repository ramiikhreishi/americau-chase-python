import mysql.connector
import pandas as pd

mydb_woogi0_1 = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='woogi0_1')

mydb_HLGD = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='HLGD')

mycursor_HLGD = mydb_HLGD.cursor()


try:
    mycursor_HLGD.execute('''CREATE TABLE HLGD.HL3_Unique_User_Logins (SELECT T1.user_id, T1.user_name, T1.Date, if(T2.School_Name IS NOT NULL, T2.School_Name, IF(T3.district_name IS NOT NULL, T3.district_name, IF(T4.tenant_name IS NOT NULL, T4.tenant_name, ""))) as "school_name",
                            IF(T2.School_ID IS NOT NULL, T2.School_ID, IF(T3.district_id IS NOT NULL, T3.district_id, IF(T4.tenant_id IS NOT NULL, T4.tenant_id, ""))) as "school_id"
                            FROM (SELECT T1.user_id, T1.user_name, LEFT(FROM_UNIXTIME(T1.time), 10) AS "Date"
                            FROM woogi0_1.wcreateusereventlog AS T1
                            WHERE T1.event = 3 AND
                            T1.app_name = "HL3.0" AND
                            T1.country_code = "US"AND
                            T1.user_name != "scottdow3" AND
                            T1.user_name != "jportik" AND
                            T1.user_name != "caiyuan07281" AND
                            T1.user_name NOT LIKE "%test%" AND
                            T1.user_name != "mbutcher"
                            GROUP BY T1.user_id , T1.user_name , `Date`) as T1
                            LEFT JOIN(SELECT * FROM HLGD.HL3_Complete_User_List where School_Name != "Freedom University" AND School_Name != "Developer Testing") AS T2 ON T1.user_id = T2.User_ID
                            LEFT JOIN (SELECT user_id, login_name, district as "district_id", district_name FROM woogi0_1.authcleveruser where login_name != "" and district_name != "") AS T3 on T1.user_id = T3.user_id
                            LEFT JOIN (SELECT user_id, dy_login_name, tenant_id, tenant_name FROM woogi0_1.classlinkuser WHERE tenant_name != "" and user_id != "0") AS T4 on T1.user_id = T4.user_id
                            WHERE if(T2.School_Name IS NOT NULL, T2.School_Name, IF(T3.district_name IS NOT NULL, T3.district_name, IF(T4.tenant_name IS NOT NULL, T4.tenant_name, ""))) != "");''')
except:
    mycursor_HLGD.execute('DROP Table HLGD.HL3_Unique_User_Logins;')
    mycursor_HLGD.execute('''CREATE TABLE HLGD.HL3_Unique_User_Logins (SELECT T1.user_id, T1.user_name, T1.Date, if(T2.School_Name IS NOT NULL, T2.School_Name, IF(T3.district_name IS NOT NULL, T3.district_name, IF(T4.tenant_name IS NOT NULL, T4.tenant_name, ""))) as "school_name",
                            IF(T2.School_ID IS NOT NULL, T2.School_ID, IF(T3.district_id IS NOT NULL, T3.district_id, IF(T4.tenant_id IS NOT NULL, T4.tenant_id, ""))) as "school_id"
                            FROM (SELECT T1.user_id, T1.user_name, LEFT(FROM_UNIXTIME(T1.time), 10) AS "Date"
                            FROM woogi0_1.wcreateusereventlog AS T1
                            WHERE T1.event = 3 AND
                            T1.app_name = "HL3.0" AND
                            T1.country_code = "US"AND
                            T1.user_name != "scottdow3" AND
                            T1.user_name != "jportik" AND
                            T1.user_name != "caiyuan07281" AND
                            T1.user_name NOT LIKE "%test%" AND
                            T1.user_name != "mbutcher"
                            GROUP BY T1.user_id , T1.user_name , `Date`) as T1
                            LEFT JOIN(SELECT * FROM HLGD.HL3_Complete_User_List where School_Name != "Freedom University" AND School_Name != "Developer Testing") AS T2 ON T1.user_id = T2.User_ID
                            LEFT JOIN (SELECT user_id, login_name, district as "district_id", district_name FROM woogi0_1.authcleveruser where login_name != "" and district_name != "") AS T3 on T1.user_id = T3.user_id
                            LEFT JOIN (SELECT user_id, dy_login_name, tenant_id, tenant_name FROM woogi0_1.classlinkuser WHERE tenant_name != "" and user_id != "0") AS T4 on T1.user_id = T4.user_id
                            WHERE if(T2.School_Name IS NOT NULL, T2.School_Name, IF(T3.district_name IS NOT NULL, T3.district_name, IF(T4.tenant_name IS NOT NULL, T4.tenant_name, ""))) != "");''')



mydb_HLGD.close()
