from database import Database

db = Database(dbname="database")

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
  


#21/2134/4/2020/paid/SEX BILL/MathiasD
class ManageBills():
  @staticmethod
  def createBill(db):
    #dict = {1:FaturaMujore, 2:RandomBill}
    print("Type 1 for FaturaMujore and type 2 For RandomBill")
    user_input = int(input())
    if user_input == 1:
      print("Enter the bill's ID, total, month, year, status,type,your username || all seperated by /: ")
      clas_input = str(input())
      cls1 = clas_input.split("/")
      cls2 = FaturaMujore(cls1[0],cls1[1],cls1[2],cls1[3],cls1[4],cls1[5],cls1[6])
      db.appendObjectInto("Product Bill",cls2)
      print("Bill added!")

      
    

    
    














class RandomBill(FaturaMujore):
  def __init__(self,ID,total,month,year,status,type_,username):
    super().__init__(self,ID,total,month,year,status,type_)
    self.username = username
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
    return "/".join([str(self.ID),str(self.total),str(self.month),str(self.year),str(self.status),self.type_,self.username])
  @classmethod
  def fromstring(cls,line):
    tokens = line.split("/")
    return cls(tokens[0],tokens[1],tokens[2],tokens[3],tokens[4],tokens[5],tokens[6])










class GasBill(RandomBill):
  def __init__(self,ID,total,month,year,status,type_,gastype,username):
    super().__init__(self,ID,total,month,year,status,type_,username)
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
    return "/".join([str(self.ID),str(self.total),str(self.month),str(self.year),str(self.status),self.type_,self.username])
  @classmethod
  def fromstring(cls,line):
    tokens = line.split("/")
    return cls(tokens[0],tokens[1],tokens[2],tokens[3],tokens[4],tokens[5],tokens[6])











class ProductBill(RandomBill):
  def __init__(self,ID,total,month,year,status,type_,producttypes,username):
    super().__init__(self,ID,total,month,year,status,type_,username)
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
    string = str(self.ID) + "/" + str(self.total) + "/" + str(self.month) +  "/" + str(self.year) + "/" + str(self.status) + "/" + str(self.type_) + "/"+ str(self.producttype)
    return string

  @classmethod
  def fromstring(cls,y):
    objects =  y.split("/")
    return cls(objects[0],objects[1],objects[2],objects[3],objects[4],objects[5],objects[6])