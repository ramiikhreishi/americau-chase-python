import mysql.connector
import pandas as pd

mydb_woogi0_1 = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='woogi0_1')

mydb_HLGD = mysql.connector.connect(user='rami', password = 'rami2023#', host= '127.0.0.1', port = 3306, database='HLGD')

mycursor_HLGD = mydb_HLGD.cursor()

try:
    mycursor_HLGD.execute('''CREATE TABLE HLGD.SkillPointsData (SELECT user_id, skill_point, if(skill = "T20_1", "T20 SK 1 - Social & Emotional Learning - Points", 
                            if(skill = "T20_2", "T20 SK 2 - Character - Points",
                            if(skill = "T20_3", "T20 SK 3 - Creativity - Points",
                            if(skill = "T20_4", "T20 SK 4 - Lifelong Learner - Points", 
                            if(skill = "T20_5", "T20 SK 5 - Health & Wellness - Points", 
                            if(skill = "T20_6", "T20 SK 6 - Resilience - Points", 
                            if(skill = "T20_7", "T20 SK 7 - Distraction Management - Points", 
                            if(skill = "T20_8", "T20 SK 8 - Technology Hardware & Coding - Points", 
                            if(skill = "T20_9", "T20 SK 9 - Trades Skills - Points", 
                            if(skill = "T20_10", "T20 SK 10 - Cultural Understanding - Points", 
                            if(skill = "T20_11", "T20 SK 11 - Civics Literacy - Points", 
                            if(skill = "T20_12", "T20 SK 12 - Environmental Literacy - Points", 
                            if(skill = "T20_13", "T20 SK 13 - Communication - Points", 
                            if(skill = "T20_14", "T20 SK 14 - Teamwork - Points", 
                            if(skill = "T20_15", "T20 SK 15 - Leadership - Points", 
                            if(skill = "T20_16", "T20 SK 16 - Digitial & Information Literacy - Points", 
                            if(skill = "T20_17", "T20 SK 17 - Entrepreneurship - Points", 
                            if(skill = "T20_18", "T20 SK 18 - Problem Solving - Points", 
                            if(skill = "T20_19", "T20 SK 19 - Financial Literacy - Points", 
                            if(skill = "T20_20", "T20 SK 20 - Habit & Goal Setting - Points", "")))))))))))))))))))) as "Long Skill", left(from_unixtime(c_time), 10) as "Date" FROM woogi0_1.wcusermissionspent WHERE skill LIKE "%T20%");''')

except:
    mycursor_HLGD.execute('DROP Table HLGD.SkillPointsData;')
    
    mycursor_HLGD.execute('''CREATE TABLE HLGD.SkillPointsData (SELECT user_id, skill_point, if(skill = "T20_1", "T20 SK 1 - Social & Emotional Learning - Points", 
                            if(skill = "T20_2", "T20 SK 2 - Character - Points",
                            if(skill = "T20_3", "T20 SK 3 - Creativity - Points",
                            if(skill = "T20_4", "T20 SK 4 - Lifelong Learner - Points", 
                            if(skill = "T20_5", "T20 SK 5 - Health & Wellness - Points", 
                            if(skill = "T20_6", "T20 SK 6 - Resilience - Points", 
                            if(skill = "T20_7", "T20 SK 7 - Distraction Management - Points", 
                            if(skill = "T20_8", "T20 SK 8 - Technology Hardware & Coding - Points", 
                            if(skill = "T20_9", "T20 SK 9 - Trades Skills - Points", 
                            if(skill = "T20_10", "T20 SK 10 - Cultural Understanding - Points", 
                            if(skill = "T20_11", "T20 SK 11 - Civics Literacy - Points", 
                            if(skill = "T20_12", "T20 SK 12 - Environmental Literacy - Points", 
                            if(skill = "T20_13", "T20 SK 13 - Communication - Points", 
                            if(skill = "T20_14", "T20 SK 14 - Teamwork - Points", 
                            if(skill = "T20_15", "T20 SK 15 - Leadership - Points", 
                            if(skill = "T20_16", "T20 SK 16 - Digitial & Information Literacy - Points", 
                            if(skill = "T20_17", "T20 SK 17 - Entrepreneurship - Points", 
                            if(skill = "T20_18", "T20 SK 18 - Problem Solving - Points", 
                            if(skill = "T20_19", "T20 SK 19 - Financial Literacy - Points", 
                            if(skill = "T20_20", "T20 SK 20 - Habit & Goal Setting - Points", "")))))))))))))))))))) as "Long Skill", left(from_unixtime(c_time), 10) as "Date" FROM woogi0_1.wcusermissionspent WHERE skill LIKE "%T20%");''')
    
    
mydb_HLGD.close()
