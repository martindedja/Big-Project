class FaturaMujore:
  def __init__(self,ID,total,month,year,status,type_,username):
    self.ID= ID
    self.total=total
    self.month=month
    self.year=year
    self.status=status
    self.type_=type_
    self.username=username
  def getValue(self):
    pass
  def toString(self):
    return "/".join([str(self.ID),str(self.total),str(self.month),str(self.year),str(self.status),self.type_,self.username])
  @classmethod
  def fromstring(cls,line):
    tokens = line.split("/")
    return cls(tokens[0],tokens[1],tokens[2],tokens[3],tokens[4],tokens[5],tokens[6])
  #def Pay(self):
  # pass
  #me kismet
  def set_(self):
    pass
  #Se mbaj mend ca esht


class RandomBill(FaturaMujore):
  def __init__(self,ID,total,month,year,status,type_,username):
    super().__init__(self,ID,total,month,year,status,type_)
    self.username = username
  def get_set(self):
    pass
        

class GasBill(RandomBill):
  def __init__(self,ID,total,month,year,status,type_,gastype):
    super().__init__(self,ID,total,month,year,status,type_)
    self.gastype=gastype

#Getters##########################################
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
  
#Setters##########################################
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

  def toString(self):
    return "/".join([str(self.ID),str(self.total),str(self.month),str(self.year),str(self.status),self.type_,self.username])
  @classmethod
  def fromstring(cls,line):
    tokens = line.split("/")
    return cls(tokens[0],tokens[1],tokens[2],tokens[3],tokens[4],tokens[5],tokens[6])
#8
class ProductBill(RandomBill):
  def __init__(self,ID,total,month,year,status,type_,producttypes):
    super().__init__(self,ID,total,month,year,status,type_)
    self.producttype=producttypes

  #Getters#########################################
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
  
#Setters#######################################
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

  def toString(self):
    #format from objects to string to save in table
    string = str(self.ID) + "/" + str(self.total) + "/" + str(self.month) +  "/" + str(self.year) + "/" + str(self.status) + "/" + str(self.type_) + "/"+ str(self.producttype)
    return string

  @classmethod
  def fromstring(cls,y):
    objects =  y.split("/")
    return cls(objects[0],objects[1],objects[2],objects[3],objects[4],objects[5],objects[6])