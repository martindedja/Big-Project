from database import Database
from prettytable import PrettyTable
from colorama import Fore
db = Database(dbname="database")
class AllBills:
  def __init__(self,ID,total,date,month,year,status,type_,product_name,username):
    self.ID= ID
    self.total=total
    self.date=date
    self.month=month
    self.year=year
    self.status=status
    self.type_=type_
    self.product_name = product_name
    self.username=username
  def toString(self):
    return "/".join([str(self.ID),str(self.total),str(self.date),str(self.month),str(self.year),str(self.status),str(self.type_),str(self.product_name),str(self.username)])
  @classmethod
  def fromstring(cls,line):
    tokens = line.split("/")
    return cls(tokens[0],tokens[1],tokens[2],tokens[3],tokens[4],tokens[5],tokens[6],tokens[7],tokens[8])

#NOT USED PLACE
#------------------Getters------------------#
  def getID(self):
    return self.ID 
  def gettotal(self):
    return self.total
  def getdate(self):
    return self.date
  def getmonth(self):
    return self.month 
  def getyear(self):
    return self.year
  def getstatus(self):
    return self.status
  def gettype_(self):
    return self.type_
  def getproduct_name(self):
    return self.product_name
  def getusername(self):
    return self.username
#------------------Setters------------------#
  def setID(self, ID):
    self.ID = ID
  def settotal(self, total):
    self.total = total
  def setdate(self,date):
    self.date = date
  def setmonth(self, month):
    self.month = month
  def setyear(self,year):
    self.year = year
  def setstatus(self, status):
    self.status = status
  def settype_(self, type_):
    self.type_ = type_
  def setproduct_name(self,product_name):
    self.product_name = product_name
  def setusername(self, username):
    self.username = username

class ManageBills():
  @staticmethod
  def createBill(db,username):
    keep_going=True
    while keep_going==True:
      try:
        ID = input("Bill ID: ")
        if len(db.getObjectsFrom("All Bills",lambda x: x.ID==ID and x.username==username))==0:
          ID=int(ID)
          if ID<1:
            print(Fore.BLACK)
            print("The ID can not be 0 or lower.")
            print(Fore.RESET)
            continue
          else:
            keep_going=False
        elif len(db.getObjectsFrom("All Bills",lambda x: x.ID==ID and x.username==username))!=0:
          print(Fore.BLACK)
          print("There is another bill with this ID.")
          print(Fore.RESET)
          continue
        else: 
          continue
      except Exception:
        continue
    keep10=True
    while keep10==True:
      try:
        total = int(input("Bill Total: "))
        if total<0:
          print(Fore.BLACK)
          print("The total can not be lower than 0.")
          print(Fore.RESET)
          continue
        else: keep10=False
      except Exception: 
        continue
    keep11=True
    while keep11==True:
      try:
        day = int(input("Day: "))
        if day>0 and day<32:
          keep11=False
        else:
          print(Fore.BLACK)
          print("Please recheck.")
          print(Fore.RESET)
          continue
      except Exception: 
        continue
    keep12=True
    while keep12==True:
      try:
        month = int(input("Month: "))
        if month>0 and month<13:
          keep12=False
        else:
          print(Fore.BLACK)
          print("Please recheck.")
          print(Fore.RESET)
          continue
      except Exception: 
        continue
    keep13=True
    while keep13==True:
      try:
        year = int(input("Year: "))
        if year>1999 and year<2021:
          keep13=False
        else:
          print(Fore.BLACK)
          print("Please recheck.")
          print(Fore.RESET)
          continue
      except Exception: 
        continue
    keep14=True
    while keep14==True:
      try:
        status = input("Bill Status(paid or not_paid): ")
        if status=="paid":
          keep14=False
        elif status=="not_paid":
          keep14=False
        else:
          print(Fore.BLACK)
          print("Please recheck.")
          print(Fore.RESET)
          continue
      except Exception: 
        continue
    keep15=True
    while keep15==True:
      try:
        print("Bill types:\nGas Bill | Electricity Bill | Monthly Bill | Water Bill | Taxes | Other")
        type_ = input("Bill Type: ")
        if type_=="Gas Bill": 
          keep15=False
        elif type_=="Electricity Bill": 
          keep15=False
        elif type_=="Monthly Bill": 
          keep15=False
        elif type_=="Water Bill": 
          keep15=False
        elif type_=="Taxes": 
          keep15=False
        elif type_=="Other": 
          keep15=False
        else:
          print(Fore.BLACK)
          print("Please recheck.")
          print(Fore.RESET)
          continue
      except Exception: 
        continue
      productname = input("Product Name: ")
      clas_input = "/".join([str(ID),str(total),str(day),str(month),str(year),str(status),str(type_),str(productname)])
    cls1=clas_input  
    cls2 = AllBills(cls1[0],cls1[1],cls1[2],cls1[3], cls1[4],cls1[5],cls1[6],cls1[7],username)  
    db.appendObjectInto("All Bills",cls2)
    print(Fore.GREEN)
    print("Bill added!")
    print(Fore.RESET)
    
  @staticmethod
  def check_smaller_date(list1,min_day,min_month,min_year):
    returned_list = []
    for bill in list1:
      infos = bill.toString().split("/")
      if min_year == int(infos[4]):
        if min_month == int(infos[3]):
          if int(min_day) > int(infos[2]):
            pass
          else:
            returned_list.append(bill)
        elif int(min_month) > int(infos[3]):
          pass
        else:
          returned_list.append(bill)
      elif int(min_year) > int(infos[4]):
        pass
      else:
        returned_list.append(bill)
    return returned_list
  @staticmethod
  def check_limit_date(list1,max_day,max_month,max_year):
    returned_list = [ ]
    for bill in list1:
      infos = bill.toString().split("/")
      if max_year == int(infos[4]):
        if max_month == int(infos[3]):
          if int(max_day) < int(infos[2]):
            pass
          else:
            returned_list.append(bill)
        elif int(max_month) < int(infos[3]):
          pass
        else:
          returned_list.append(bill)
      elif int(max_year) < int(infos[4]):
        pass
      else:
        returned_list.append(bill)
    return returned_list
  @staticmethod
  def filterBill(db,username):
    print("\nPress 1 to filter by Type: ")
    print("Press 2 to filter by Deadline: ")
    print("Press 3 to filter by Total: ")
    print("Press 4 to go back to main menu: ")
    user_input= int(input(">\n"))
    if user_input == 1:
      type_input = input("Give the type of bill you'd like to search: ")
      if len(db.getObjectsFrom("All Bills", lambda x: x.username == username))!=0:
        filtered_list = db.getObjectsFrom("All Bills", lambda x: x.type_ == type_input and x.username == username)
        if len(filtered_list) != 0:
          ManageBills.show_my_filtered_bills(db, filtered_list)
    elif user_input == 2:
      min_deadline = input("Start date dd/mm/yyyy format: ").split("/")
      max_deadline = input("End date  dd/mm/yyyy format: ").split("/")
      min_day,min_month,min_year = int(min_deadline[0]), int(min_deadline[1]), int(min_deadline[2])
      max_day,max_month,max_year = int(max_deadline[0]), int(max_deadline[1]), int(max_deadline[2])
      list1 = db.getObjectsFrom("All Bills", lambda x:True)
      min_date_checked_bills = ManageBills.check_smaller_date(list1, min_day,min_month,min_year)
      in_deadline_bills = ManageBills.check_limit_date(min_date_checked_bills, max_day, max_month, max_year)
      ManageBills.show_my_filtered_bills(db, in_deadline_bills)
    elif user_input == 3:
      min_total = int(input("Enter min total: "))
      max_total = int(input("Enter max total: ")) 
      if len(db.getObjectsFrom("All Bills", lambda x: x.username == username))!=0:
        a = db.getObjectsFrom("All Bills", lambda x: min_total<= int(x.total) <= max_total and x.username == username )
        if len(a)!=0:
          ManageBills.show_my_filtered_bills(db, a)
    else:
      pass
  @staticmethod
  def deleteBill(db,username):
    print("Enter the ID and Type of the bill you want to delete : ")
    ID = input("ID = ")
    Type = input("Type = ")
    db.deleteObjectsFrom("All Bills",lambda a: a.ID == ID and a.username==username and a.type_ == Type)
    print(Fore.GREEN)
    print("Bill successfully deleted!")
    print(Fore.RESET)
  @staticmethod
  def unpaid_bills(db,username):
    a = (db.getObjectsFrom("All Bills", lambda x : x.username == username and x.status=="not_paid"))
    if len(a)!=0:
      ManageBills.show_my_filtered_bills(db, a)
      print("Press 1 to select a bill and declare it as paid or press 2 to go to the main menu.")
      choice=int(input(">"))
      if choice==2:
        pass
      elif choice==1:
        thatid=str(input("Please enter the bill's ID:"))
        ap=db.getObjectsFrom("All Bills", lambda x : x.username == username and x.ID==thatid)
        ap[0].setstatus("paid")
        w=db.getObjectsFrom("All Bills",lambda x:x.username==username and x.ID!=thatid)
        w.append(ap[0])
        db.overwriteObjectsInto("All Bills", w)
        print(Fore.YELLOW)
        print("Bill declared as paid.")     
        print(Fore.RESET)  
    else:
      print(Fore.ORANGE)
      print("You do not have any unpaid bills")
      print(Fore.RESET)
      pass
  @staticmethod
  def showmybills(db,username):
    if len(db.getObjectsFrom("All Bills", lambda x : x.username == username))!=0:
      a = (db.getObjectsFrom("All Bills", lambda x : x.username == username))
      t = PrettyTable(['ID','Total','Date','Month','Year','Status','Type','Product Name','Username'])
      for bill in a:
        t.add_row([bill.ID, bill.total, bill.date, bill.month, bill.year, bill.status, bill.type_, bill.product_name, bill.username])
      print(t)
  @staticmethod
  def show_my_filtered_bills(db, filtered_bills):
    if len(filtered_bills) != 0:
      
      t = PrettyTable(['ID','Total','Date','Month','Year','Status','Type','Product Name','Username'])
      for bill in filtered_bills:
        t.add_row([bill.ID, bill.total, bill.date, bill.month, bill.year, bill.status, bill.type_, bill.product_name, bill.username])
      print(t)