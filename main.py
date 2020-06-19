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
    all_accounts=db.getObjectsFrom("Accounts",condition= lambda a:True)
    if len(all_accounts) ==0:
      print("Register the account.")
      #TODO add new account
    else:
      print("Press 1 for login, 2 to register and 3 for exiting.")
      a=int(input())
       
      if a==1:
        pass
        #TODO login
      elif a==2:
        pass
        #TODO crete new Account
      elif a==3:
        pass
        #TODO exit
      else:
        continue


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







