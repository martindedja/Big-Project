#accounts and login
#DONE AND WORKING
from database import Database

db = Database(dbname="database")

class Account:

  
  def __init__(self,Username,Email,Password,FullName,PhoneNumber,Age):
    self.username = Username
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
  

#Getters#########################################
  def getUsername(self):
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
  
#Setters#######################################
  def setUsername(self,username):
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


class Login:
  def __init__(self, username, password):
    self.username = username
    self.password = password
  
  @classmethod
  def fromstring(cls,y):
    objects =  y.split("/")
    return cls(objects[0],objects[1],objects[2],objects[3],objects[4],objects[5])

  def CheckCredentials(self):
    object = db.getObjectsFrom("Accounts",lambda x: x.username == self.username)
    if object[0].password == self.password:
      print("Success")
      #REDIRECT ASK NIKOLIN
    else:
      print("Wrong credentials")
#MathiasD/mathias.dariu@gmail.com/2341/MathiasDariu/069321433215/18  


class Accounts():
  @staticmethod
  def createAcc(db):
    class_input = input("Enter the account's username, email, password, fullname, phoneno and age, all divided by /")
    cl1 = class_input.split("/")
    cl2 = Account(cl1[0],cl1[1],cl1[2],cl1[3],cl1[4],int(cl1[5]))
    db.appendObjectInto("Accounts",cl2)

  @staticmethod
  def deleteAcc(db):
    username = input("Enter account's username: ")
    password = input("Enter password to confirm deletion: ")
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
    password = input("Enter your account's password: ")
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
