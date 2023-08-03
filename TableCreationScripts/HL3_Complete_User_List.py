import mysql.connector
import pandas as pd

mydb_woogi0_1 = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='woogi0_1')

mydb_HLGD = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='HLGD')

mycursor_woogi0_1 = mydb_woogi0_1.cursor()

mycursor_HLGD = mydb_HLGD.cursor()

try:
    mycursor_HLGD.execute('''create table HLGD.HL3_Complete_User_List (SELECT Distinct User_ID, User_Name, School_Name, School_ID FROM (SELECT if(ULT.user_id is NULL, ULT.DA_user_id, ULT.user_id) as "User_ID", if(ULT.user_name is NULL, ULT.DA_user_name, ULT.user_name) as "User_Name", if(ULT.school_name IS NULL, ULT.DA_school_name, ULT.school_name) as "School_Name", if(ULT.school_id IS NULL, ULT.DA_school_id, ULT.school_id) as "School_ID" FROM
                                (Select T1.user_id, T1.user_name, T4.school_name, T4.school_id, DA.user_id As "DA_user_id", DA.user_name As "DA_user_name", DA.s_id As "DA_school_id", DA.school_name As "DA_school_name" From(select user_id, user_name from woogi0_1.wcreateusereventlog where event = 4 AND app_name = "HL3.0" GROUP BY user_id, user_name) as T1
                                JOIN (select user_id, team_id from woogi0_1.wcteamuser group by user_id, team_id) as T2 ON T1.user_id = T2.user_id
                                JOIN (select team_id, village_id from woogi0_1.wcreatecityvillage) as T3 on T2.team_id = T3.team_id
                                JOIN (SELECT IG.village_id, SSO.school_id, SSO.school_name, SSO.sign_id, SSO.district_name, SSO.kind, SSO.c_time FROM (select id as "village_id", name from woogi0_1.wcreatecityconfig3) as IG
                                JOIN (select id, school_id, school_name, sign_id, sign_name as "district_name", kind, c_time  from woogi0_1.`auththirdpartschoolrelation`) as SSO on IG.name=SSO.school_name) as T4 on T3.village_id = T4.village_id
                                RIGHT JOIN (select D1.woogi_user_id as "user_id", D1.username as "user_name", D1.s_id, D2.s_name as "school_name", D2.district_id, D2.district_name from woogi0_1.dynamouser as D1
                                LEFT JOIN (select s_id, s_name, district_id, district_name from woogi0_1.dynamoschool) as D2 on D1.s_id = D2.s_id WHERE D2.s_name IS NOT NULL) as DA on T1.user_id = DA.user_id
                                UNION
                                Select T1.user_id, T1.user_name, T4.school_name, T4.school_id, DA.user_id As "DA_user_id", DA.user_name As "DA_user_name", DA.s_id As "DA_school_id", DA.school_name As "DA_school_name" From(select user_id, user_name from woogi0_1.wcreateusereventlog where event = 4 AND app_name = "HL3.0" GROUP BY user_id, user_name) as T1
                                JOIN (select user_id, team_id from woogi0_1.wcteamuser group by user_id, team_id) as T2 ON T1.user_id = T2.user_id
                                JOIN (select team_id, village_id from woogi0_1.wcreatecityvillage) as T3 on T2.team_id = T3.team_id
                                JOIN (SELECT IG.village_id, SSO.school_id, SSO.school_name, SSO.sign_id, SSO.district_name, SSO.kind, SSO.c_time FROM (select id as "village_id", name from woogi0_1.wcreatecityconfig3) as IG
                                JOIN (select id, school_id, school_name, sign_id, sign_name as "district_name", kind, c_time  from woogi0_1.`auththirdpartschoolrelation`) as SSO on IG.name=SSO.school_name) as T4 on T3.village_id = T4.village_id
                                LEFT JOIN (select D1.woogi_user_id as "user_id", D1.username as "user_name", D1.s_id, D2.s_name as "school_name", D2.district_id, D2.district_name from woogi0_1.dynamouser as D1
                                    LEFT JOIN (select s_id, s_name, district_id, district_name from woogi0_1.dynamoschool) as D2 on D1.s_id = D2.s_id WHERE D2.s_name IS NOT NULL) as DA on T1.user_id = DA.user_id) as ULT
                                UNION
                                SELECT distinct T1.user_id, T1.user_name, T4.sign_name as "School_Name", T4.clone_modstorm_id as "School_ID"
                                FROM (select user_id, user_name FROM woogi0_1.wcreateusereventlog group by user_id, user_name) as T1
                                LEFT JOIN (SELECT user_id, team_id FROM woogi0_1.wcteamuser) AS T2 ON T1.user_id = T2.user_id
                                LEFT JOIN (SELECT team_id, village_id FROM woogi0_1.wcreatecityvillage) AS T3 ON T2.team_id = T3.team_id
                                LEFT JOIN (SELECT * FROM woogi0_1.auththirdpartschool) AS T4 ON T3.village_id = T4.clone_modstorm_id
                                WHERE T4.clone_modstorm_id = "73159") as T1);''')
except:
    mycursor_HLGD.execute('DROP Table HLGD.HL3_Complete_User_List;')
    mycursor_HLGD.execute('''create table HLGD.HL3_Complete_User_List (SELECT Distinct User_ID, User_Name, School_Name, School_ID FROM (SELECT if(ULT.user_id is NULL, ULT.DA_user_id, ULT.user_id) as "User_ID", if(ULT.user_name is NULL, ULT.DA_user_name, ULT.user_name) as "User_Name", if(ULT.school_name IS NULL, ULT.DA_school_name, ULT.school_name) as "School_Name", if(ULT.school_id IS NULL, ULT.DA_school_id, ULT.school_id) as "School_ID" FROM
                                (Select T1.user_id, T1.user_name, T4.school_name, T4.school_id, DA.user_id As "DA_user_id", DA.user_name As "DA_user_name", DA.s_id As "DA_school_id", DA.school_name As "DA_school_name" From(select user_id, user_name from woogi0_1.wcreateusereventlog where event = 4 AND app_name = "HL3.0" GROUP BY user_id, user_name) as T1
                                JOIN (select user_id, team_id from woogi0_1.wcteamuser group by user_id, team_id) as T2 ON T1.user_id = T2.user_id
                                JOIN (select team_id, village_id from woogi0_1.wcreatecityvillage) as T3 on T2.team_id = T3.team_id
                                JOIN (SELECT IG.village_id, SSO.school_id, SSO.school_name, SSO.sign_id, SSO.district_name, SSO.kind, SSO.c_time FROM (select id as "village_id", name from woogi0_1.wcreatecityconfig3) as IG
                                JOIN (select id, school_id, school_name, sign_id, sign_name as "district_name", kind, c_time  from woogi0_1.`auththirdpartschoolrelation`) as SSO on IG.name=SSO.school_name) as T4 on T3.village_id = T4.village_id
                                RIGHT JOIN (select D1.woogi_user_id as "user_id", D1.username as "user_name", D1.s_id, D2.s_name as "school_name", D2.district_id, D2.district_name from woogi0_1.dynamouser as D1
                                LEFT JOIN (select s_id, s_name, district_id, district_name from woogi0_1.dynamoschool) as D2 on D1.s_id = D2.s_id WHERE D2.s_name IS NOT NULL) as DA on T1.user_id = DA.user_id
                                UNION
                                Select T1.user_id, T1.user_name, T4.school_name, T4.school_id, DA.user_id As "DA_user_id", DA.user_name As "DA_user_name", DA.s_id As "DA_school_id", DA.school_name As "DA_school_name" From(select user_id, user_name from woogi0_1.wcreateusereventlog where event = 4 AND app_name = "HL3.0" GROUP BY user_id, user_name) as T1
                                JOIN (select user_id, team_id from woogi0_1.wcteamuser group by user_id, team_id) as T2 ON T1.user_id = T2.user_id
                                JOIN (select team_id, village_id from woogi0_1.wcreatecityvillage) as T3 on T2.team_id = T3.team_id
                                JOIN (SELECT IG.village_id, SSO.school_id, SSO.school_name, SSO.sign_id, SSO.district_name, SSO.kind, SSO.c_time FROM (select id as "village_id", name from woogi0_1.wcreatecityconfig3) as IG
                                JOIN (select id, school_id, school_name, sign_id, sign_name as "district_name", kind, c_time  from woogi0_1.`auththirdpartschoolrelation`) as SSO on IG.name=SSO.school_name) as T4 on T3.village_id = T4.village_id
                                LEFT JOIN (select D1.woogi_user_id as "user_id", D1.username as "user_name", D1.s_id, D2.s_name as "school_name", D2.district_id, D2.district_name from woogi0_1.dynamouser as D1
                                    LEFT JOIN (select s_id, s_name, district_id, district_name from woogi0_1.dynamoschool) as D2 on D1.s_id = D2.s_id WHERE D2.s_name IS NOT NULL) as DA on T1.user_id = DA.user_id) as ULT
                                UNION
                                SELECT distinct T1.user_id, T1.user_name, T4.sign_name as "School_Name", T4.clone_modstorm_id as "School_ID"
                                FROM (select user_id, user_name FROM woogi0_1.wcreateusereventlog group by user_id, user_name) as T1
                                LEFT JOIN (SELECT user_id, team_id FROM woogi0_1.wcteamuser) AS T2 ON T1.user_id = T2.user_id
                                LEFT JOIN (SELECT team_id, village_id FROM woogi0_1.wcreatecityvillage) AS T3 ON T2.team_id = T3.team_id
                                LEFT JOIN (SELECT * FROM woogi0_1.auththirdpartschool) AS T4 ON T3.village_id = T4.clone_modstorm_id
                                WHERE T4.clone_modstorm_id = "73159") as T1);''')
    
    
mydb_HLGD.close()

mydb_woogi0_1.close()
