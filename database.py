import os
from os import path
class Database:
    def __init__(self,dbname,dbpath="."):
        # set the destination path for the database folder
        self.mainpath = dbpath+path.sep+dbname
        if(not path.exists(self.mainpath)):
            # if folder does not exists create a new one
            os.mkdir(self.mainpath)
        # create a dictionary that will hold tables
        self.tables = {}
    # creates a file if it does ont exists
    def createtableifnotexists(self,tname,ttype,toObject):
        # check if is created before
        if(not path.exists(self.mainpath+path.sep+tname)):
            # add specific entry into the dictionary
            self.tables[tname]=Table(self.mainpath+path.sep+tname,ttype,toObject)
            # create respective file
            fd = open(self.mainpath+path.sep+tname,"w")
            fd.close()
        else :
            # science the file already exists just add the entry into the dictionary
            self.tables[tname]=Table(self.mainpath+path.sep+tname,ttype,toObject)
    # get a list of objects from a specific table. you can also filter by a lambda function
    def getObjectsFrom(self,tname,condition=lambda a:True):
        # find table data from the dictionary
        table = self.tables[tname]
        # open the file
        with (open(table.getpath(),"r")) as fp:
            records = []
            # read all lines
            lines = fp.readlines()
            for line in lines:
                # construct the object by the specific function
                record = table.toObject(line)
                # if object fullfill the condition then add into list
                print("testing",condition(record))
                if( condition(record)):
                    records.append(record)
            # close the file and then return the ist of selected objects
            fp.close()
            return records
        return(101,"file not found")
    # this method just adds the objects in the end of the file
    def appendObjectsInto(self,tname,records):
        table = self.tables[tname]
        # after taking table data open file
        with open(table.getpath() ,"a") as fp:
            for  record in records:
                # if object is of specififed type
                if table.checkType(record):
                    # write it into the file
                    fp.write(record.toString()+"\n")
            fp.close()
    def appendObjectInto(self,tname,obj):
        self.appendObjectsInto(tname,[obj])
    # this function deletes records specifying a specific function
    def deleteObjectsFrom(self,tname,condition=lambda x:False):
        # select the respective table from dictionary
        table = self.tables[tname]
        # read all records
        with (open(table.getpath(),"r")) as fp:
            # read all lines of data one line for one object
            lines = fp.readlines()
            fp.close()
        # write onnly those that do not fullfill the condition
        with(open(table.getpath(),"w") )as fp:
            # for each line
            for line in lines:
                # construct the apropriate object using the
                # function toObject of the respective table
                record = table.toObject(line)
                if(not condition(record)):
                    fp.write(line)
            fp.close()
        return(101,"file not found")
    # this function writes objects in a file but the
    # old data is allways lost
    def overwriteObjectsInto(self,tname,newobjects):
        # select the table
        table = self.tables[tname]
        # open the file
        with open(table.getpath() ,"w") as fp:
            # for each object
            for  newobject in newobjects:
                # check if it is an apropriate type for this table
                if table.checkType(newobject):
                    # dump the record into the table
                    fp.write(newobject.toString()+"\n")
            fp.close()
class Table :
    # a table is an istance that is defined by
    # a path where the objects are stored (lines)
    # a type stating types of objects stored in file
    # a toObject method that converts a line into an object
    # of specified type
    def __init__(self,tpath,ttype,toObject):
        self.__tpath = tpath
        self.__type = ttype
        self.__toObject = toObject
    # table destination in file system
    def getpath(self):return self.__tpath
    # checks if an object is of table specified type
    def checkType(self,ttype):return self.__type==type(ttype)
    # returns a line into an object of specified type of table
    def toObject(self,line):return self.__toObject(line)
# simple base object
class BaseObject:
    def __init__(self,ID):
        self._ID = ID
    def setID(self,newID):self._ID = newID
    def getID(self):return self._ID
    # mandatory method for each class storable to be created
    # returns a line holding information for a specific object
    def toString(self):
        # all fields separated by comma ending the line with \n
        return str(self._ID)
    #gets a line  of string and from that line the object is constructed
    # methods toString and fromLine are inverse of each other as
    #  class.fromString(a.toString()).toString() =  a.toString()
    @classmethod
    def fromLine(cls,line):
        tokens = line.split(",")
        return cls(tokens[0])
# create three simple objects
#Obj1 = BaseObject(1)
#Obj2 = BaseObject(2)
#Obj3 = BaseObject(3)
# create the database object
#db = Database(dbname="database1")
# create table if not exists pass as argument table name, object type to sav
# and the function to convert a line into an object
#db.createtableifnotexists("baseobjects",BaseObject,BaseObject.fromLine)
# append the objects in the table. you can append one or more objects
#db.appendObjectsInto("baseobjects",[Obj1,Obj2,Obj3])
# table state  1\n2\n3\n
#db.overwriteObjectsInto("baseobjects",[BaseObject(1),BaseObject(3),BaseObject(7)])
# table state 1\n2\n7\n
# get the objects
#a = db.getObjectsFrom("baseobjects",lambda c:True)
#print(a)
class Date:
    def __init__(self,year,month,day):
        self._year = year
        self._month = month
        self._day = day
    def toString(self):
        return str(self._year)+"/"+str(self._month)+"/"+str(self._day)
    @classmethod
    def fromString(cls,pattern):
        fields = pattern.split("/")
        return cls(fields[0],fields[1],fields[2])
class storeBill:
    def __init__(self,id,date,user,amount):
        self._id = id
        self._date = date
        self._user = user
        self._amount = amount
    def toString(self):
        return str(self._id)+","+self._date.toString()+","+str(self._user)+","+str(self._amount)
    @classmethod
    def fromline(cls,line):
        fields = line.split(",")
        id = int(fields[0])
        date = Date.fromString(fields[1])
        user = fields[2]
        amount = float(fields[3])
        return cls(id,date,user,amount)
print("test 1")
bill1 = storeBill(1,Date.fromString("2020/12/1"),"hadoop",20.5)
bill2 = storeBill(2,Date.fromString("2020/11/1"),"hadoop",10.5)
bill3 = storeBill(3,Date.fromString("2020/10/1"),"hadoop",120.5)
bill4 = storeBill(4,Date.fromString("2020/09/1"),"hadoop",21.5)
bill5 = storeBill(5,Date.fromString("2020/08/1"),"hadoop",24.5)
# bill1  1 "date"  "hadoop"   20.5
def func(x):
    if(x._user != "hadoop"):
        return True
    return False
lambda x:x._user !="hadoop"
db1 = Database("bills")
db1.createtableifnotexists("storebill",storeBill,storeBill.fromline)
#db1.appendObjectInto("storebill",bill1)
#db1.appendObjectsInto("storebill",[bill1, bill2])
def fun1(x):
    if x._id == 1:
        return True
    return  False
#obj  = db1.getObjectsFrom("storebill",fun1)
#db1.deleteObjectsFrom("storebill",func)
def func(x):return x._id ==3
db1.overwriteObjectsInto("storebill",[bill4, bill5])
#def ofilter(x):return x._id ==2
#print([c.toString() for c in  db1.getObjectsFrom("storebill",ofilter)])
