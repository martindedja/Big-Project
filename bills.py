from database import Database
from prettytable import PrettyTable



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
  @staticmethod
  def createclassBill(db,user):
    print("Enter the bill's ID, total,date, month, year, status, type , product name all seperated by /: ")
    class_input = str(input())
    cl1 = class_input.split("/")
    if len(cl1) == 8 and cl1[1].isdigit() and cl1[2] and cl1[3] and cl1[4]:
      if cl1[5] == 'not_paid' or 'paid':
        cl2 = AllBills(cl1[0],cl1[1],cl1[2],cl1[3],cl1[4],cl1[5],cl1[6],cl1[7],user)
        db.appendObjectInto("All Bills",cl2)
      else:
        print("Bill status error! write not_paid or paid!!")
    else:
      print("Wrong bill structure")

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

#21/2134/4/2020/paid/FaturaMujore/MathiasD
#21/2134/4/2020/paid/RandomBill/MathiasD
#21/2134/4/2020/paid/GasBill/MathiasD/Nafte
#21/2134/4/2020/paid/ProductBill/MathiasD/Patate

class ManageBills():
  @staticmethod
  def createBill(db, user):
    #dict = {1:FaturaMujore, 2:RandomBill}
    print("Enter the bill's ID, total, day,month, year, status,type,product name|| all seperated by /: ")
    keep_going=True
    while keep_going==True:
      clas_input = str(input())
      cls1 = clas_input.split("/")
      if len(cls1) == 8 and cls1[1].isdigit() and cls1[2].isdigit() and cls1[3].isdigit() and cls1[4].isdigit():
        if cls1[5] == 'not_paid' or cls1[5] == 'paid':
          if int(cls1[2])>31 or int(cls1[2])<1:
            print("Check the date.")
            continue
          elif int(cls1[3])<1 or int(cls1[3])>12:
            print("Check the month.")
            continue
          elif int(cls1[4])<2000:
            print("Check the year:")
            continue
          else:
            cls2 = AllBills(cls1[0],cls1[1],cls1[2],cls1[3], cls1[4],cls1[5],cls1[6],cls1[7],user)
            db.appendObjectInto("All Bills",cls2)
            print("Bill added!")
            keep_going=False
        else:
          print("Check the status")
      else:
        print("Incorrect date or bill structure")

  @staticmethod
  def check_smaller_date(list1,min_day,min_month,min_year):
    returned_list = [ ]
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
    print("Press 1 to filter by Type: ")
    print("Press 2 to filter by Deadline: ")
    print("Press 3 to filter by Total: ")

    user_input= input()
    if user_input.isdigit():
      user_input = int(user_input)
    else:
      print('Wrong input')
    if user_input == 1:
      type_input = input("Give the type of bill you'd like to search: ")
      if len(db.getObjectsFrom("All Bills", lambda x: x.username == username))!=0:
        filtered_list = db.getObjectsFrom("All Bills", lambda x: x.type_ == type_input and x.username == username)
        if len(filtered_list) != 0:
          ManageBills.show_my_filtered_bills(db, filtered_list)
      
      
    
    elif user_input == 2:
      min_deadline = input("Start date dd/mm/yyyy format: ").split("/")
      if len(min_deadline) == 3 and min_deadline[0].isdigit() and min_deadline[1].isdigit() and min_deadline[2].isdigit():
        max_deadline = input("End date  dd/mm/yyyy format: ").split("/")
        if len(max_deadline) == 3 and max_deadline[0].isdigit() and max_deadline[1].isdigit() and max_deadline[2].isdigit():
          min_day,min_month,min_year = int(min_deadline[0]), int(min_deadline[1]), int(min_deadline[2])
          max_day,max_month,max_year = int(max_deadline[0]), int(max_deadline[1]), int(max_deadline[2])
          list1 = db.getObjectsFrom("All Bills", lambda x:True)
          min_date_checked_bills = ManageBills.check_smaller_date(list1, min_day,min_month,min_year)
          in_deadline_bills = ManageBills.check_limit_date(min_date_checked_bills, max_day, max_month, max_year)
          for bill in in_deadline_bills:
            print(bill.date, bill.month, bill.year,"\n")
        else:
          print("Incorrect end date!")
      else:
        print("Incorrect start date!")
    elif user_input == 3:
      min_total = int(input("Enter min total: "))
      max_total = int(input("Enter max total: "))
      if min_total.isdigit() and max_total.isdigit():
        if len(db.getObjectsFrom("All Bills", lambda x: x.username == username))!=0:
          a = db.getObjectsFrom("All Bills", lambda x: min_total<= int(x.total) <= max_total and x.username == username )
          if len(a)!=0:
            ManageBills.show_my_filtered_bills(db, a)
    else:
    	print("\n")
    	return

  @staticmethod
  def deleteBill(db,username):
    print("Enter the ID and Type of the bill you want to delete : ")
    ID = input("ID = ")
    Type = input("Type = ")
    db.deleteObjectsFrom("All Bills",lambda a: a.ID == ID and a.username==username and a.type_ == Type)
    print("Bill succssesfully deleted!")
  @staticmethod
  def ModifyBill(db):
    print("Press 1 to modify gas bills\nPress 2 to modify monthly bill\n Press 3 to modify Product bill \n press 4 to modify a random bill")
    choice=input(">")
    if choice=='1':
      print("Press 1 to change ID \nPress 2 to modify \n Press 3 to modify Product bill \n press 4 to modify a random bill")
      pass
    pass

  @staticmethod
  def unpaid_bills(db,username):
    a = (db.getObjectsFrom("All Bills", lambda x : x.username == username and x.status=="not_paid"))
    if len(a)!=0:
      ManageBills.show_my_filtered_bills(db, a)
      print("Press 1 to select a bill and declare it as paid or press 2 to go to the main menu.")
      choice=input(">")
      if choice.isdigit():
        choice = int(choice)

      if choice==2:
        pass
      elif choice==1:
        thatid=str(input("Please enter the bill's ID:"))
        ap=db.getObjectsFrom("All Bills", lambda x : x.username == username and x.ID==thatid)
        ap[0].setstatus("paid")
       
        w=db.getObjectsFrom("All Bills",lambda x:x.username==username and x.ID!=thatid)
        w.append(ap[0])
        db.overwriteObjectsInto("All Bills", w)
        print("Bill declared as paid.")       
    else:
      print("You do not have any unpaid bills")
      pass
  #2861/2134/28/07/2019/paid/GasBill/Nafte/MathiasD
  
  
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
      print("okay")
      t = PrettyTable(['ID','Total','Date','Month','Year','Status','Type','Product Name','Username'])
      for bill in filtered_bills:
        t.add_row([bill.ID, bill.total, bill.date, bill.month, bill.year, bill.status, bill.type_, bill.product_name, bill.username])
      print(t)