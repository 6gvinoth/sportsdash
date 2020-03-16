import mysql.connector

mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      passwd="personify",
      database="adfsports"
)

import pandas as pd
data=pd.read_clipboard(header=None)
mycursor=mydb.cursor()
for name in data[0].to_list():
	sql = "INSERT INTO teams (name, team) VALUES (%s, %s)"
	val = (name, "Team A")
	mycursor.execute(sql, val)
for name in data[1].to_list():
	sql = "INSERT INTO teams (name, team) VALUES (%s, %s)"
	val = (name, "Team B")
	mycursor.execute(sql, val)
for name in data[2].to_list():
	sql = "INSERT INTO teams (name, team) VALUES (%s, %s)"
	val = (name, "Team C")
	mycursor.execute(sql, val)
mydb.commit()
