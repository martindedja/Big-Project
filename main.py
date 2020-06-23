from database import Database
from bills import *
from identity import Account,Accounts,Login
from reports import *
from SpecialFunctions import *
#Grupi 4 esht jet <3




def startSession(db,User):
  while(True):
  #ManageBills.createBill(db)
  # menuja kryesore 
    #manage bills
    #manage Account
    #reports
    #FindMonthlyTotal.findTotal(self,MathiasD)
    print("Press 1 to add bills:")
    print("Press 2 to filer bills:")
    print("Press 3 to delete bills:")
    print("Press 4 to modify bills:")
    print("Press 5 to show all your bills: ")
    print("Press 0 to log out:")
    
    choice = int(input())

    if(choice==1):
      ManageBills.createBill(db)

    elif (choice == 2):
      ManageBills.filterBill(db)
      
    elif (choice == 3):
      ManageBills.deleteBill(db)

    elif (choice == 0):
      return
    
    elif (choice == 4):
      pass
      
    elif (choice == 5):
      ManageBills.showmybills(db)
    else:
      continue



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
  db.createtableifnotexists("All Bills", AllBills,AllBills.fromstring)


  db.createtableifnotexists("Accounts",Account,Account.fromstring)
  user=None
  
  while(True):

    # check if there is any account 
    all_accounts=db.getObjectsFrom("Accounts",condition= lambda a:True)
    if len(all_accounts) == 0:
      print("Register the account: ")
      Accounts.createAcc(db)
    print("Press 1 for Login\nPress 2 to register\nPress 3 for exiting\nPress 4 to change your password")
    a=int(input())     
    if a==1:
      user=Login.CheckCredentials(db)
      if user==None:
        continue  
      else:
         startSession(db,user)
    elif a==2:
      Accounts.createAcc(db)
    elif a==3:
      return
      
    else:
      continue

    
   



  
if __name__ == '__main__':
  main()