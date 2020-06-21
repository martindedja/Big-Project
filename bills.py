from database import Database

db = Database(dbname="database")

global username
class FaturaMujore:
  def __init__(self,ID,total,month,year,status,type_,username):
    self.ID= ID
    self.total=total
    self.month=month
    self.year=year
    self.status=status
    self.type_=type_
    self.username=username

  def toString(self):
    return "/".join([str(self.ID),str(self.total),str(self.month),str(self.year),str(self.status),self.type_,self.username])
  @classmethod
  def fromstring(cls,line):
    tokens = line.split("/")
    return cls(tokens[0],tokens[1],tokens[2],tokens[3],tokens[4],tokens[5],tokens[6])

  @staticmethod
  def createclassBill(db):
    print("Enter the bill's ID, total, month, year, status, type all seperated by /: ")
    class_input = str(input())
    cl1 = class_input.split("/")
    cl2 = FaturaMujore(cl1[0],cl1[1],cl1[2],cl1[3],cl1[4],cl1[5],cl1[6])
    db.appendObjectInto("Product Bill",cl2)
  #def Pay(self):
  # pass
  #me kismet
#------------------Getters------------------#
  def getID(self):
    return self.ID 
  def gettotal(self):
    return self.total
  def getmonth(self):
    return self.month 
  def getyear(self):
    return self.year
  def getstatus(self):
    return self.status
  def gettype_(self):
    return self.type_
  def getUsername(self):
    return self.username
#------------------Setters------------------#
  def setID(self, ID):
      self.ID = ID
  def settotal(self, total):
      self.total = total
  def setmonth(self, month):
      self.month = month
  def setyear(self,year):
      self.year = year
  def setstatus(self, status):
      self.status = status
  def settype_(self, type_):
      self.type_ = type_
  def setUsername(self, username):
      self.username = username



class RandomBill(FaturaMujore):
  def __init__(self,ID,total,month,year,status,type_,username):
    super().__init__(ID,total,month,year,status,type_,username)
#------------------Getters------------------#
  def getID(self):
    return self.ID
  def gettotal(self):
    return self.total
  def getmonth(self):
    return self.month
  def getyear(self):
    return self.year
  def getstatus(self):
    return self.status
  def gettype_(self):
    return self.type_
  def getUsername(self):
    return self.username
#------------------Setters------------------#
  def setID(self, ID):
    self.ID = ID
  def settotal(self, total):
    self.total = total
  def setmonth(self, month):
    self.month = month
  def setyear(self,year):
    self.year = year
  def setstatus(self, status):
    self.status = status
  def settype_(self, type_):
    self.type_ = type_
  def setUsername(self, username):
    self.username = username


  def toString(self):
    return "/".join([str(self.ID),str(self.total),str(self.month),str(self.year),str(self.status),str(self.type_),str(self.username)])
    
  @classmethod
  def fromstring(cls,line):
    tokens = line.split("/")
    return cls(tokens[0],tokens[1],tokens[2],tokens[3],tokens[4],tokens[5],tokens[6])










class GasBill(RandomBill):
  def __init__(self,ID,total,month,year,status,type_,username,gastype):
    super().__init__(ID,total,month,year,status,type_,username)
    self.gastype=gastype

#------------------Getters------------------#
  def getID(self):
    return self.ID
  def gettotal(self):
    return self.total
  def getmonth(self):
    return self.month
  def getyear(self):
    return self.year
  def getstatus(self):
    return self.status
  def gettype_(self):
    return self.type_
  def getgastype(self):
    return self.gastype
  def getUsername(self):
    return self.username
#------------------Setters------------------#
  def setID(self, ID):
    self.ID = ID
  def settotal(self, total):
    self.total = total
  def setmonth(self, month):
    self.month = month
  def setyear(self,year):
    self.year = year
  def setstatus(self, status):
    self.status = status
  def settype_(self, type_):
    self.type_ = type_
  def setgastype(self, gastype):
    self.gastype = gastype
  def setUsername(self, username):
    self.username = username

  def toString(self):
    return "/".join([str(self.ID),str(self.total),str(self.month),str(self.year),str(self.status),str(self.type_),str(self.username),str(self.gastype)])
  @classmethod
  def fromstring(cls,line):
    tokens = line.split("/")
    return cls(tokens[0],tokens[1],tokens[2],tokens[3],tokens[4],tokens[5],tokens[6],tokens[7])











class ProductBill(RandomBill):
  def __init__(self,ID,total,month,year,status,type_,username,producttypes):
    super().__init__(ID,total,month,year,status,type_,username)
    self.producttype=producttypes

  #------------------Getters------------------#
  def getID(self):
    return self.ID
  def gettotal(self):
    return self.total
  def getmonth(self):
    return self.month
  def getyear(self):
    return self.year
  def getstatus(self):
    return self.status
  def gettype_(self):
    return self.type_
  def getproducttypes(self):
    return self.producttypes
  def getUsername(self):
    return self.username
  
#------------------Setters------------------#
  def setID(self,ID):
    self.ID = ID
  def settotal(self, total):
    self.total = total
  def setmonth(self, month):
    self.month = month
  def setyear(self, year):
    self.year = year
  def setstatus(self, status):
    self.status = status
  def settype_(self, type_):
    self.type_ = type_
  def setproducttypes(self, producttypes):
    self.producttypes = producttypes
  def setUsername(self, username):
    self.username = username

  def toString(self):
    #format from objects to string to save in table
    string = str(self.ID) + "/" + str(self.total) + "/" + str(self.month) +  "/" + str(self.year) + "/" + str(self.status) + "/" + str(self.type_) + "/"+ str(self.username) + "/" + str(self.producttype) 
    return string

  @classmethod
  def fromstring(cls,y):
    objects =  y.split("/")
    return cls(objects[0],objects[1],objects[2],objects[3],objects[4],objects[5],objects[6],objects[7])





#21/2134/4/2020/paid/FaturaMujore/MathiasD
#21/2134/4/2020/paid/RandomBill/MathiasD
#21/2134/4/2020/paid/GasBill/MathiasD/Nafte
#21/2134/4/2020/paid/ProductBill/MathiasD/Patate

class ManageBills():
  @staticmethod
  def createBill(db):
    #dict = {1:FaturaMujore, 2:RandomBill}
    print("Press 1 to add Monthly Bill")
    print("Press 2 to add Random Bill")
    print("Press 3 to add Gas Bill")
    print("Press 4 to add Product Bill")
    user_input = int(input())
    if user_input == 1:
      print("Enter the bill's ID, total, month, year, status,type,your username || all seperated by /: ")
      clas_input = str(input())
      cls1 = clas_input.split("/")
      cls2 = FaturaMujore(cls1[0],cls1[1],cls1[2],cls1[3],cls1[4],cls1[5],cls1[6])
      db.appendObjectInto("All Bills",cls2)
      print("Bill added!")
    elif user_input == 2:
      print("Enter the bill's ID, total, month, year, status,type,your username || all seperated by /: ")
      clas_input = str(input())
      cls1 = clas_input.split("/")
      cls2 = RandomBill(cls1[0],cls1[1],cls1[2],cls1[3],cls1[4],cls1[5],cls1[6])
      db.appendObjectInto("All Bills",cls2)
      print("Bill added!")
    
    elif user_input == 3:
      print("Enter the bill's ID, total, month, year, status,type,gas type and your username || all seperated by /: ")
      clas_input = str(input())
      cls1 = clas_input.split("/")
      cls2 = GasBill(cls1[0],cls1[1],cls1[2],cls1[3],cls1[4],cls1[5],cls1[6],cls1[7])
      db.appendObjectInto("All Bills",cls2)
      print("Bill added!")

    elif user_input == 4:
      print("Enter the bill's ID, total, month, year, status,type,products type andyour username || all seperated by /: ")
      clas_input = str(input())
      cls1 = clas_input.split("/")
      cls2 = ProductBill(cls1[0],cls1[1],cls1[2],cls1[3],cls1[4],cls1[5],cls1[6],cls1[7])
      db.appendObjectInto("All Bills",cls2)
      print("Bill added!")
    
    else:
      pass


  @staticmethod
  def filerBill(db):
    print("Press 1 to filter by Total: ")
    print("Press 2 to filter by Deadline: ")
    print("Press 3 to filter by Type: ")
    user_input= int(input())
    if user_input == 3:
      print("Press 1 for Monthly Bill: ")
      print("Press 2 for Gas Bill: ")
      print("Press 3 for Product Bill: ")
      user_input2 = int(input())
      if user_input2 == 1:
        returned_bills = db.getObjectsFrom("All Bills", lambda x: type(x) == FaturaMujore)
        for bill in returned_bills:
          print(bill.username, bill.type_)
        
      elif user_input2 == 2:
        pass
      elif user_input2 == 3:
        pass
      else:
        pass
    elif user_input == 1:
      pass
    
    elif user_input == 2:
      pass
    
    else:
      pass

  
  @staticmethod
  def deleteBill(db):
    pass

  @staticmethod
  def showmybills(db):
    pass


class FindMonthlyTotal:
  @staticmethod
  def findTotal(self,username):

    a =db.getObjectsFrom("All Bills",lambda x : x.username == "MathiasD")
    print(a[0])