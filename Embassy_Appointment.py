import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="7676919622"
)
mycursor = mydb.cursor()

class Appointment:
    def __init__(self, user, date, time, purpose):
        self.user = user
        self.date = date
        self.time = time
        self.purpose = purpose

    def get_details(self):
        return f'Appointment for {self.user} on {self.date} at {self.time} for {self.purpose}'

class AppointmentScheduler:
    def createdb():
        try:
            mycursor.execute("CREATE DATABASE Embassy")
        except Exception:
            print('Already Created DB')

    def useDB():
        try:
            mycursor.execute("USE Embassy")
            print("using DB")
        except Exception:
            print('Already Used DB')
    
    def createTable():
        try:
            mycursor.execute("CREATE TABLE  MyTable(user varchar(30),date varchar(20),time varchar(30),purpose varchar(30))")
        except Exception:
            print('Already Created Table')
    
    def schedule_appointments():
        user=input("Enter user's name: ")
        date=input("Enter appointment date: ")
        time=input("Enter appointment time: ")
        purpose=input("Enter Purpose of appointment: ")
        try:
            mycursor.execute("INSERT INTO MyTable(user,date,time,purpose) values(%s,%s,%s,%s)",(user,date,time,purpose))
            mydb.commit()
            print('Inserted Successfully!')          
        except Exception: 
            print('Already Inserted Data into Table')

    def view_appointments():
        mycursor.execute("SELECT * FROM MyTable")
        appointments = mycursor.fetchall()
        for appointment in appointments:
            print(Appointment(*appointment).get_details())
            
    
    def update_Appointment():
        date=input("Enter new date: ")
        user=input("Enter the name of user whose data to be updated: ")
        try:
            mycursor.execute("UPDATE MyTable SET date=%s WHERE user=%s",(date,user))
            mydb.commit()
            print('Updated Successfully!')
        except Exception:
            print('Already Inserted Data into Table')
            
    def delete_Appointment():
        user=input("Enter name of user to be deleted: ")
        try:
            mycursor.execute("DELETE FROM MyTable WHERE user=%s",(user,))
            mydb.commit()
            print('Deleted Successfully!')
        except Exception:
            print('Issue while Deleting')
        
Appsedul=AppointmentScheduler
Appsedul.createdb()
Appsedul.useDB()
Appsedul.createTable()
Appsedul.schedule_appointments()
Appsedul.update_Appointment()
Appsedul.delete_Appointment()
Appsedul.view_appointments()
