import mysql.connector

#connection.object
mydb =mysql.connector.connect(host="localhost",
                                  user="root",
                                  password="Pradhan@12",
                                  database='BANK',)
mycursor=mydb.cursor()
s='''create table  CustomerDetail
     (first_name char(30),middle_name char(30),last_name char(30),
      DOB char(40),gender char(10),nationality char(40),
      maritial_status char(50),address varchar(50),phone_number varchar(50),
      mail_id varchar(100))'''
#mycursor.execute(s)


#Table Insertion
first_name = input("Enter your First Name (along with Mr./Mrs./Miss): ")
middle_name = input("Enter your Middle Name: ")
last_name = input("Enter your Last Name: ")
DOB = input("Enter your date of birth: ")
gender = input("Gender(F/M): ")
nationality = input("Nationality: ")
maritial_status = input("Marital Status:(Married/Unmarried) ")
address = input("Enter your current address: ")
phone_number = input("Contact no.: ")
mail_id = input("mail ID: ")

#Table execution of the values
mycursor.execute('''
INSERT INTO CustomerDetail(first_name, middle_name, last_name, DOB, gender, nationality, maritial_status, address, phone_number,mail_id)
VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
''',
(first_name, middle_name, last_name, DOB, gender, nationality, maritial_status, address, phone_number,mail_id))
mydb.commit()
print( "Data entered successfully" )