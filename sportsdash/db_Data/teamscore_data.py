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
data=pd.read_csv("1teamscore.csv")

#remove Existing table
try:
    query="drop table teamsscore"
    mycursor.execute(query)
except:
    pass
#create Teams table
query="create table teamsscore (TeamMatch varchar(100),Sports varchar(100),Point int,Wonby varchar(10),Lossby varchar(10))"
mycursor.execute(query)

data=data.fillna('')

for index,row in data.iterrows():
    
    sql="INSERT INTO teamsscore (TeamMatch,Sports,Point,Wonby,Lossby) VALUES (%s,%s,%s,%s,%s)"
    val=(row["TeamMatch"],row["Sports"],row["Point"],row["Wonby"],row["Lossby"])
    mycursor.execute(sql, val)
mydb.commit()
