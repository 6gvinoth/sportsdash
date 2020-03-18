import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="personify",
      database="adfsports"
)

mycursor=mydb.cursor()

#input data
data=pd.read_csv("Teams.csv")

#remove Existing table
try:
    query="drop table teams"
    mycursor.execute(query)
except:
    pass
#create Teams table
query="create table teams (name varchar(100),team varchar(100))"
mycursor.execute(query)

#insert values
for index,row in data.iterrows():
        sql = "INSERT INTO teams (name, team) VALUES (%s, %s)"
        val = (row['name'],row['team'])
        mycursor.execute(sql, val)
    
mydb.commit()
#___PointSystem_______________________________________________________________________________________________________

data=pd.read_csv("PointsSystems.csv")
data=data.fillna('')
try:
    query="drop table pointsystem"
    mycursor.execute(query)
except:
    pass
#create Teams table
query="create table pointsystem (SNo varchar(10),Game varchar(100),Category varchar(100),SubCategory varchar(100),Fixture varchar(100),\
WinningPtGame int,MaxPointTeam int,MinPlayerReq varchar(10) ,TotalPoints varchar(10))"
mycursor.execute(query)

#insert values
for index,row in data.iterrows():
        
        sql = "INSERT INTO  pointsystem (SNo,Game,Category,SubCategory,Fixture,WinningPtGame,MaxPointTeam, MinPlayerReq,TotalPoints) \
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (row['S.No'], row['Game'], row['Category'], row['Sub Category'], row['Fixture'], row['Winning Pt/Game'], row['Max Point/Team'], row['Min Player Req'], row['Total Points'])
        mycursor.execute(sql, val)
mydb.commit()

#___Fixture1_______________________________________________________________________________________________________
data=pd.read_csv("Fixture1.csv")

try:
    query="drop table fixture1"
    mycursor.execute(query)
except:
    pass
query="create table fixture1 (Fixture1 varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO fixture1 (Fixture1) VALUES (%s)"
    val=(row["Fixture 1"],)
    mycursor.execute(sql, val)
mydb.commit()


#___Fixture2_______________________________________________________________________________________________________
data=pd.read_csv("Fixture2.csv")

try:
    query="drop table fixture2"
    mycursor.execute(query)
except:
    pass
query="create table fixture2 (Fixture2 varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO fixture2 (Fixture2) VALUES (%s)"
    val=(row["Fixture 2"],)
    mycursor.execute(sql, val)
mydb.commit()


#___Fixture3_______________________________________________________________________________________________________
data=pd.read_csv("Fixture3.csv")

try:
    query="drop table fixture3"
    mycursor.execute(query)
except:
    pass
query="create table fixture3 (Fixture3 varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO fixture3 (Fixture3) VALUES (%s)"
    val=(row["Fixture 3"],)
    mycursor.execute(sql, val)
mydb.commit()

#___Fixture4_______________________________________________________________________________________________________
data=pd.read_csv("Fixture4.csv")

try:
    query="drop table fixture4"
    mycursor.execute(query)
except:
    pass
query="create table fixture4 (Fixture4 varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO fixture4 (Fixture4) VALUES (%s)"
    val=(row["Fixture 4"],)
    mycursor.execute(sql, val)
mydb.commit()


#___Fixture5_______________________________________________________________________________________________________
data=pd.read_csv("Fixture5.csv")

try:
    query="drop table fixture5"
    mycursor.execute(query)
except:
    pass
query="create table fixture5 (Fixture5 varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO fixture5 (Fixture5) VALUES (%s)"
    val=(row["Fixture 5"],)
    mycursor.execute(sql, val)
mydb.commit()


#___Fixture6_______________________________________________________________________________________________________
data=pd.read_csv("Fixture6.csv")

try:
    query="drop table fixture6"
    mycursor.execute(query)
except:
    pass
query="create table fixture6 (Fixture6 varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO fixture6 (Fixture6) VALUES (%s)"
    val=(row["Fixture 6"],)
    mycursor.execute(sql, val)
mydb.commit()

#___Fixture7_______________________________________________________________________________________________________
data=pd.read_csv("Fixture7.csv")

try:
    query="drop table fixture7"
    mycursor.execute(query)
except:
    pass
query="create table fixture7 (Fixture7 varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO fixture7 (Fixture7) VALUES (%s)"
    val=(row["Fixture 7"],)
    mycursor.execute(sql, val)
mydb.commit()


#___Fixture8_______________________________________________________________________________________________________
data=pd.read_csv("Fixture8.csv")

try:
    query="drop table fixture8"
    mycursor.execute(query)
except:
    pass
query="create table fixture8 (Fixture8 varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO fixture8 (Fixture8) VALUES (%s)"
    val=(row["Fixture 8"],)
    mycursor.execute(sql, val)
mydb.commit()




#___carrom_______________________________________________________________________________________________________
data=pd.read_csv("carrom.csv")

try:
    query="drop table carrom"
    mycursor.execute(query)
except:
    pass
query="create table carrom (Matchdate varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO carrom (Matchdate) VALUES (%s)"
    val=(row["Match date"],)
    mycursor.execute(sql, val)
mydb.commit()

#___cricket_______________________________________________________________________________________________________
data=pd.read_csv("cricket.csv")

try:
    query="drop table cricket"
    mycursor.execute(query)
except:
    pass
query="create table cricket(Match_ varchar(100),Date varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="""INSERT INTO cricket (Match_,Date) VALUES (%s,%s)"""
    val=(row["Match"],row["Date"])
    mycursor.execute(sql, val)
mydb.commit()


#___batmintion_______________________________________________________________________________________________________
data=pd.read_csv("batminton.csv")

try:
    query="drop table batminton"
    mycursor.execute(query)
except:
    pass
query="create table batminton (Matchdate varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO batminton (Matchdate) VALUES (%s)"
    val=(row["Match date"],)
    mycursor.execute(sql, val)
mydb.commit()


#___chess_______________________________________________________________________________________________________
data=pd.read_csv("chess.csv")

try:
    query="drop table chess"
    mycursor.execute(query)
except:
    pass
query="create table chess (Matchdate varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO chess (Matchdate) VALUES (%s)"
    val=(row["Match date"],)
    mycursor.execute(sql, val)
mydb.commit()



#___tabletennis_______________________________________________________________________________________________________
data=pd.read_csv("tabletennis.csv")

try:
    query="drop table tabletennis"
    mycursor.execute(query)
except:
    pass
query="create table tabletennis (Matchdate varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO tabletennis (Matchdate) VALUES (%s)"
    val=(row["Match date"],)
    mycursor.execute(sql, val)
mydb.commit()




#___cricket_______________________________________________________________________________________________________
data=pd.read_csv("counterstrike.csv")

try:
    query="drop table counterstrike"
    mycursor.execute(query)
except:
    pass
query="create table counterstrike(Match_ varchar(100),Date varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="""INSERT INTO counterstrike (Match_,Date) VALUES (%s,%s)"""
    val=(row["Match"],row["Date"])
    mycursor.execute(sql, val)
mydb.commit()

#___counterstrike_______________________________________________________________________________________________________
data=pd.read_csv("counterstrike.csv")

try:
    query="drop table counterstrike"
    mycursor.execute(query)
except:
    pass
query="create table counterstrike(Match_ varchar(100),Date varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="""INSERT INTO counterstrike (Match_,Date) VALUES (%s,%s)"""
    val=(row["Match"],row["Date"])
    mycursor.execute(sql, val)
mydb.commit()



#___football_______________________________________________________________________________________________________
data=pd.read_csv("football.csv")

try:
    query="drop table football"
    mycursor.execute(query)
except:
    pass
query="create table football(Match_ varchar(100),Date varchar(100))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="""INSERT INTO football (Match_,Date) VALUES (%s,%s)"""
    val=(row["Match"],row["Date"])
    mycursor.execute(sql, val)
mydb.commit()

