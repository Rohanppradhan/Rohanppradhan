
import mysql.connector

#connection.object
mydb =mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="Pradhan@12",)
                                  #database="Bank")
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE library (name varchar(40), class varchar(50), section varchar(50))")

#mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)