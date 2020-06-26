from database import Database
from bills import *
from identity import Account,Accounts,Login
from report import Reports
from Graph import *
from report import *
#Grupi 4 esht jet <3

def startSession(db,User):
  while(True):
  #ManageBills.createBill(db)
  # menuja kryesore 
    #manage bills
    #manage Account
    #reports
    #FindMonthlyTotal.findTotal(self,MathiasD)
    print("Press 1 to add bills.")
    print("Press 2 to filer bills.")
    print("Press 3 to delete bills.")
    print("Press 4 to show all your bills. ")
    print("Press 5 to acces report pannel.")
    print("Press 6 to acces graph.")
    print("Press 7 to show all your unpaid bills.")
    print("Press 8 to show some website to gather information about paying your bills.")
    print("Press 9 to change your password.")
    print("Press 0 to log out.\n")

    choice = input(">")

    if(choice=='1'):
      ManageBills.createBill(db,User)

    elif (choice == '2'):
      ManageBills.filterBill(db,User)
      
    elif (choice == '3'):
      ManageBills.deleteBill(db,User)
      
    elif (choice == '4'):
      ManageBills.showmybills(db,User)
    elif (choice == '5'):
      print("\n\nWelcome to the report pannel!\n")
      print("Press 1 to get a daily report, for all the bills paid in the same day!")
      print("Press 2 to get a mothly report, for all the bills paid within a same month!")
      print("Press 3 to get a yearly report, for all the bills paid within a same year!\n\n")
      usr_input = input("Input: ")
      if usr_input == '1':
        date = input("Please give us the day you'd like a report of divided with / :")
        print("The daily report of the", date, "is", Reports.showDailyReport(db,User,date))
      elif usr_input == '2':
        date = input("Give the month and year divded with / :")
        print("The monthly report of the", date, "is", Reports.showMonthlyReport(db, User, date))
      elif usr_input == '3':
        date = input("Give the year: ")
        print("The monthly report of the", date, "is", Reports.showYearlyReport(db, User, date))
      else:
        pass
    elif (choice == '6'):
      CreateGraph(db,User)
    elif (choice == '7'):
      ManageBills.unpaid_bills(db,User)
    elif(choice=='8'):
      paying()
    elif(choice == '9'):
      Accounts.changePassword(db)
    elif (choice == '0'):
      User == None
      break
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
  user = None
  
  while(True):
    # check if there is any account 
    all_accounts=db.getObjectsFrom("Accounts", lambda a:True)
    if len(all_accounts) == 0:
      print("Register the account: ")
      Accounts.createAcc(db)
    print("Press 1 for Login\nPress 2 to register\nPress 3 for exiting")

    a = input(">")
    if a=='1':
      user=Login.CheckCredentials(db)
      if user==None:
        continue  
      else:
         startSession(db,user)
    elif a=='2':
      Accounts.createAcc(db)
    elif a=='3':
      return
    
    elif a=='4':
      pass
    else:
      print("Not a valid choice!")
      continue

if __name__ == '__main__':
  main()