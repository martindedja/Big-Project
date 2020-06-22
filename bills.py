from database import Database
db = Database(dbname="database")
global username
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
  def createclassBill(db):
    print("Enter the bill's ID, total,date, month, year, status, type , product name,username all seperated by /: ")
    class_input = str(input())
    cl1 = class_input.split("/")
    cl2 = AllBills(cl1[0],cl1[1],cl1[2],cl1[3],cl1[4],cl1[5],cl1[6],cl1[7],cl1[8])
    db.appendObjectInto("All Bills",cl2)
  #def Pay(self):
  # pass
  #me kismet
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
  def getUsername(self):
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
  def setUsername(self, username):
    self.username = username

#21/2134/4/2020/paid/FaturaMujore/MathiasD
#21/2134/4/2020/paid/RandomBill/MathiasD
#21/2134/4/2020/paid/GasBill/MathiasD/Nafte
#21/2134/4/2020/paid/ProductBill/MathiasD/Patate

class ManageBills():
  @staticmethod
  def createBill(db):
    #dict = {1:FaturaMujore, 2:RandomBill}
    print("Enter the bill's ID, total, date,month, year, status,type,your username || all seperated by /: ")
    keep_going=True
    while keep_going==True:
      try:
        clas_input = str(input())
        cls1 = clas_input.split("/")
        if cls1[2]>31 or cls1<1:
          print("Check the date.")
          continue
        elif cls1[3]<1 or cls1[3]>12:
          print("Check the month.")
          continue
        elif len(list(cls1[4]))!=4:
          print("Check the year.")
          continue
        else:
          cls2 = AllBills(cls1[0],cls1[1],cls1[2],cls1[3], cls1[4],cls1[5],cls1[6],cls1[7],cls1[8])
          db.appendObjectInto("All Bills",cls2)
          print("Bill added!")
          keep_going=False
      except Exception:
        pass

  @staticmethod
  def check_smaller_date(list1,min_day,min_month,min_year):
    returned_list = [ ]
    for bill in list1:
      infos = bill.toString().split("/")
      if min_year == infos[4]:
        if min_month == infos[3]:
          if min_day > infos[2]:
            pass
          else:
            returned_list.append(bill)
        elif min_month > infos[3]:
          pass
        else:
          returned_list.append(bill)
      elif min_year > infos[2]:
        pass
      else:
        returned_list.append(bill)
    return returned_list
  

  @staticmethod
  def check_limit_date(list1,max_day,max_month,max_year):
    returned_list = [ ]
    for bill in list1:
      infos = bill.toString().split("/")
      if max_year == infos[4]:
        if max_month == infos[3]:
          if max_day < infos[2]:
            pass
          else:
            returned_list.append(bill)
        elif max_month < infos[3]:
          pass
        else:
          returned_list.append(bill)
      elif max_year < infos[4]:
        pass
      else:
        returned_list.append(bill)

    return returned_list
  
#20/2/2020
#21/3/2021
#19/1/2019
      




  @staticmethod
  def filterBill(db):
    print("Press 1 to filter by Total: ")
    print("Press 2 to filter by Deadline: ")

    user_input= int(input())

    if user_input == 1:
      pass
    
    elif user_input == 2:
      min_deadline = input("Enter date in dd/mm/yyyy format: ").split("/")
      max_deadline = input("Enter date in dd/mm/yyyy format: ").split("/")
      min_day,min_month,min_year = min_deadline[0], min_deadline[1], min_deadline[2]
      max_day,max_month,max_year = max_deadline[0], max_deadline[1], max_deadline[2]

      list1 = db.getObjectsFrom("All Bills", lambda x:True)
      min_date_checked_bills = ManageBills.check_smaller_date(list1, min_day,min_month,min_year)
      in_deadline_bills = ManageBills.check_limit_date(min_date_checked_bills, max_day, max_month, max_year)
      for bill in in_deadline_bills:
        print(bill.date, bill.month, bill.year,"\n")
    

    else:
      pass

  
  @staticmethod
  def deleteBill(db):
    print("Enter the ID and Type of the bill you want to delete : ")
    ID = input("ID = ")
    Type = input("Type = ")
    db.deleteObjectsFrom(Type,lambda a: a.ID == ID )
    print("Bill succssesfully deleted!")
  @staticmethod
  def ModifyBill(db):
    print("Press 1 to modify gas bills\nPress 2 to modify monthly bill\n Press 3 to modify Product bill \n press 4 to modify a random bill")
    choice=input(">")
    if choice==1:
      print("Press 1 to change ID \nPress 2 to modify \n Press 3 to modify Product bill \n press 4 to modify a random bill")
      pass
    pass


  @staticmethod
  def showmybills(db):
    usn=input("Username:")
    if len(db.getObjectsFrom("All Bills",lambda x: x.username==usn))>=1:
      bills1=db.getObjectsFrom("All Bills",lambda x: x.username==usn)
      for bill in bills1:
        print(bill.username ,"\n")
      if len(db.getObjectsFrom("All Bills",lambda x:True))==0:
        print("You do not have any bills registered")
      else:
        print("Error Occured! Please try again!")

class FindMonthlyTotal:
  @staticmethod
  def findTotal(db,username):# mos duhet db dhe jo self ktu?
    a =db.getObjectsFrom("Monthly Bill",lambda x : x.username == "MathiasD")
    print(a[0])