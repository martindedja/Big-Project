from database import Database
from bills import *
from identity import Account,Accounts,Login
from reports import *

#Grupi 4 esht jet


def main():
  print("          (         )            (               ")
  print(" (        )\ )   ( /(            )\ )         )  ")
  print(" )\ )    (()/(   )\())      (   (()/(      ( /(  ")
  print("(()/(     /(_)) ((_)\       )\   /(_))     )\()) ")
  print(" /(_))_  (_))     ((_)   _ ((_) (_))      ((_)\  ")
  print("(_)) __| | _ \   / _ \  | | | | | _ \    | | (_) ")
  print("  | (_ | |   /  | (_) | | |_| | |  _/    |_  _|  ")
  print("   \___| |_|_\   \___/   \___/  |_|        |_|   ")

  db = Database(dbname="database")
  # create tables here 
  db.createtableifnotexists("Monthly Bill", FaturaMujore,FaturaMujore.toString)
  db.createtableifnotexists("Random Bill", RandomBill,RandomBill.toString)
  db.createtableifnotexists("Gas Bill", GasBill,GasBill.toString)
  db.createtableifnotexists("Product Bill",ProductBill,ProductBill.toString)

  db.createtableifnotexists("Accounts",Account,Account.fromstring)
  user=None
  while(True):
    # check if there is any account 
    all_accounts=db.getObjectsFrom("Accounts",condition= lambda a:True)
    if len(all_accounts) == 0:
      print("Register the account: ")
      Accounts.createAcc(db)
      print("Press 1 for login, 2 to register and 3 for exiting.")
      a=int(input())     
      if a==1:
        Login.CheckCredentials(db)
      elif a==2:
        Accounts.createAcc(db)
      elif a==3:
        pass
        #TODO exit
      else:
        continue


    # if login sucesfull 
    while(True):
      ManageBills.createBill(db)
      # menuja kryesore 
      #manage bills
      #manage Account
      #reports
      #FindMonthlyTotal.findTotal(self,MathiasD)

      print("Press 1 to add bills:")
      print("Press 2 to filer bills:")
      print("Press 3 to delete bills:")
      print("Press 4 to modify bills:")
      choice = int(input())
      #if else  if else 
      #choice = input("Press 1: ")
      if(choice==1):
        ManageBills.createBill(db)

      elif choice == 2:
        ManageBills.filerBill(db)
        #ManageAccount
      elif choice == 3:
        Manage.deleteBill(db)
        #Reports

      #else:
      pass



  
if __name__ == '__main__':
  main()