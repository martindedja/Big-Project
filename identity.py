#accounts and login
#DONE AND WORKING
from database import Database
import getpass
'''
import smtplib, ssl
import email.utils
def sendemail(receiver,content):
  port = 465  # For SSL
  smtp_server = "smtp.gmail.com"
  sender_email = "group4python@gmail.com"  
  password =("mihallaris")
  context = ssl.create_default_context()
  with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, receiver, content)
'''
class Account:

  
  def __init__(self,username,Email,Password,FullName,PhoneNumber,Age):
    self.username = username
    self.email = Email
    self.password = Password
    self.full_name = FullName
    self.phone_no = PhoneNumber
    self.age = Age

  def toString(self):
    #format from objects to string to save in table
    string = str(self.username) + "/" + str(self.email) + "/" + str(self.password) +  "/" + str(self.full_name) + "/" + str(self.phone_no) + "/" + str(self.age)
    return string

  @classmethod
  def fromstring(cls,y):
    objects =  y.split("/")
    return cls(objects[0],objects[1],objects[2],objects[3],objects[4],objects[5])
  

#------------------Getters------------------#
  def getusername(self):
    return self.username
  def getEmail(self):
    return self.email
  def getPassword(self):
    return self.password
  def getFullName(self):
    return self.full_name
  def getPhoneNumber(self):
    return self.phone_no
  def getAge(self):
    return self.age

#------------------Setters------------------#
  def setusername(self,username):
    self.username = username
  def setEmail(self, email):
    self.email = email
  def setPassword(self, password):
    self.password = password
  def setFullName(self, fullname):
    self.full_name = fullname
  def setPhoneNumber(self, phonenumber):
    self.phone_no = phonenumber
  def setAge(self, age):
    self.age = age


class Login():
  @staticmethod
  def CheckCredentials(db):
    username = input("Username: ")
    object = db.getObjectsFrom("Accounts",lambda x: x.username == username)
    password = getpass.getpass("Password: ")
    if object[0].password == password:
      print("Success")
      return username
    else:
      print("Wrong credentials")
      return None
  
#MathiasD/mathias.dariu@gmail.com/2341/MathiasDariu/069321433215/18  


class Accounts():
  @staticmethod
  def createAcc(db):
    
    print("Enter the account's username, email, password, fullname, phone no and age, all divided by /: ")
    class_input = str(input())
    cl1 = class_input.split("/")
    # check first if all data is correctly entered by the user 
    # TODO 
    cl2 = Account(cl1[0],cl1[1],cl1[2],cl1[3],cl1[4],int(cl1[5]))
    # Validate object
    db.appendObjectInto("Accounts",cl2)
    #sendemail(str(cl1[1]),"Subject: Welcome to #KesmetGroup.\
    #Glad we have you, enjoy your time using our app.")


  @staticmethod
  def deleteAcc(db):
    username = input("Enter account's username: ")
    password = getpass.getpass("Enter password to confirm deletion: ")
    if (len(db.getObjectsFrom("Accounts", lambda x:x.username == username)) == 1):
      object1 = db.getObjectsFrom("Accounts",lambda x: x.username == username)
      if (object1[0].password == password):
        db.deleteObjectsFrom("Accounts",lambda a: a.password == password and a.username == username)
        print("Account succssesfully deleted!")
    else:
      print("Username does not exist!")

  @staticmethod
  def modifyAcc(db):
    username = input("Enter your account's username: ")
    password = getpass.getpass("Enter your account's password: ")
    if (len(db.getObjectsFrom("Accounts", lambda x:x.username == username)) != 0):
      old_account = db.getObjectsFrom("Accounts",lambda x: x.username == username)
      if (old_account[0].password == password):
        new_password = input("Enter your new password: ")
        old_account[0].setPassword(new_password)
        all_accounts = db.getObjectsFrom("Accounts", lambda x:x.username != username)
        all_accounts.append(old_account[0])
        db.overwriteObjectsInto("Accounts", all_accounts)
    else:
      print("Username does not exist!")
