from database import Database
from bills import ProductBill
from identity import Account
from reports import *


def main():
  # loading 
  db = Database(dbname="database")
  # create tables here 
  db.createtableifnotexists("Product Bill", ProductBill,ProductBill.fromstring)
  db.createtableifnotexists("Accounts",Account,Account.fromstring)
  while(True):
    # check if there is any account 
    # if it is ask for log in 
    # login 
    # register 
    # 
    # if login sucesfull 
    while(True):
      # menuja kryesore 
      #if else  if else 
      choice = input(">")
      if(choice==1):
        while(False):
          pass
        pass
      else:
        pass










    






if __name__ == '__main__':
    main()







