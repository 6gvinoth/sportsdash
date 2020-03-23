#score board
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
data=pd.read_csv("batting.csv")

#remove Existing table
try:
    query="drop table batting"
    mycursor.execute(query)
except:
    pass
#create Teams table
query="create table batting (Name varchar(100),Runs int,Balls int,4s int,6s int,SR int,Team varchar(10),Match_ varchar(10))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO batting (Name,Runs,Balls,4s,6s,SR,Team,Match_) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(row["Name"],row["Runs"],row["Balls"],row["4s"],row["6s"],row["SR"],row["Team"],row["Match"])
    mycursor.execute(sql, val)
mydb.commit()


#input data
data=pd.read_csv("bowling.csv")

#remove Existing table
try:
    query="drop table bowling"
    mycursor.execute(query)
except:
    pass
#create Teams table
query="create table bowling (Bowler varchar(100),O int,M int,R int,W int,ER int,Team varchar(10),Match_ varchar(10))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO bowling (Bowler,O,M,R,W,ER,Team,Match_) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(row["Bowler"],row["O"],row["M"],row["R"],row["W"],row["ER"],row["Team"],row["Match"])
    mycursor.execute(sql, val)
mydb.commit()


