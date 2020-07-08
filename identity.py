from database import Database
from bills import ManageBills
import getpass
from colorama import Fore
from checkit import *
class Account:
  def __init__(self,username,Email,Password,FullName,PhoneNumber,Age):
    self.username = username
    self.email = Email
    self.password = Password
    self.full_name = FullName
    self.phone_no = PhoneNumber
    self.age = Age
  def toString(self):
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
    if len(object)!=0:
      if object[0].password == password:
        print(Fore.GREEN)
        print("You shall pass!")
        print(Fore.RESET)
        return username
      else:
        print(Fore.RED)
        print("YOU SHALL NOT PASS!!")
        print(Fore.RESET)
        return None
    else:
      print(Fore.RED)
      print("This username does not exist.")
      print(Fore.RESET)
      return None
class Accounts():
  @staticmethod
  def createAcc(db):
    keep1=True
    while keep1==True:
      try:
        username = input("Enter username: ")
        if len(db.getObjectsFrom("Accounts",lambda x:x.username==username))!=0:
          print(Fore.BLACK)
          print("Please enter a different username.")
          print(Fore.RESET)
          continue
      except Exception:
        continue
      else:
        keep1=False
    keep2=True
    while keep2==True:
      try:
        email = input("Enter email: ")
        if check(email)==True:
          keep2=False
        else:
          print(Fore.BLACK)
          print("Please recheck.")
          print(Fore.RESET)
          continue
      except Exception: 
        print(Fore.BLACK)
        print("Please recheck.")
        print(Fore.RESET)
        continue 
    keep5=True
    while keep5==True:
      try:
        password = getpass.getpass("Enter password: ")
        confirm=getpass.getpass("Please reenter the password:")
        if password==confirm: keep5=False
        else:
          print(Fore.BLACK)
          print("Please recheck.")
          print(Fore.RESET)
        continue
      except Exception:
        continue
      

    fullname = input("Enter full name: ")
    keep4=True
    while keep4==True:
      try:
        phone_no = input("Enter phone number: ")  
        if len(phone_no)==10:
          keep4=False
        elif len(phone_no)==12:
          keep4=False
        else:
          print(Fore.BLACK)
          print("Please recheck.")
          print(Fore.RESET)
          continue
      except Exception:
        (Fore.BLACK)
        print("Please recheck.") 
        (Fore.RESET)
        continue
    keep3=True
    while keep3==True:
      try:
        age = int(input("Enter age: "))
      except Exception: continue
      else: keep3=False
    class_input = "/".join([str(username), str(email), str(password), str(fullname), str(phone_no), str(age)])
    cl1 = class_input.split("/")
    cl2 = Account(cl1[0],cl1[1],cl1[2],cl1[3],cl1[4],int(cl1[5]))
    db.appendObjectInto("Accounts",cl2)
    print(Fore.GREEN)
    print("Account created.")
    print(Fore.RESET)
  @staticmethod
  def deleteAcc(db,username):
    password = getpass.getpass("Enter password again to confirm deletion: ")
    if (len(db.getObjectsFrom("Accounts", lambda x:x.username == username)) == 1):
      object1 = db.getObjectsFrom("Accounts",lambda x: x.username == username)
      if (object1[0].password == password):
        db.deleteObjectsFrom("Accounts",lambda a: a.password == password and a.username == username)
        db.deleteObjectsFrom("All Bills",lambda a: a.username==username)
        print(Fore.RED)
        print("Account succssesfully deleted!")
        print(Fore.RESET)
      else:
        print(Fore.RED)
        print("An Error Occured! Please Try Again!")
        print(Fore.RESET)
    else:
      print(Fore.RED)
      print("Wrong password.")
      print(Fore.RESET)
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
        print(Fore.RED)
        print("An Error Occured! Please Try Again!")
        print(Fore.RESET)
    else:
      print(Fore.RED)
      print("Username does not exist!")
      print(Fore.RESET)
  @staticmethod
  def changePassword(db,username):
    password = input("Enter password: ")
    a = (db.getObjectsFrom("Accounts", lambda x : x.username == username and x.password==password))
    if len(a)!=0:
      print("Press 1 to change password or press 2 to go to the main menu.")
      choice=int(input(">"))
      if choice==2:
        pass
      elif choice==1:
        new_password=str(input("Please enter the new password:"))
        ap=db.getObjectsFrom("Accounts", lambda x : x.username == username and x.password==password)
        ap[0].setPassword(new_password)
        w=db.getObjectsFrom("Accounts",lambda x:x.username==username and x.password!=password)
        w.append(ap[0])
        db.overwriteObjectsInto("Accounts", w)
        print("\nPassword Changed Successfully\n")
      else:
        print(Fore.RED)
        print("Unknown character value!")
        print(Fore.RESET)       
    else:
      print(Fore.RED)
      print("Error")
      print(Fore.RESET)