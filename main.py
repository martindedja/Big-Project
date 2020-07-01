from database import Database
from bills import *
from identity import *
from report import Reports
from Graph import *
from report import *
from clear_screen import clear
from time import sleep 
#Grupi 4 esht jet <3
import colorama
from colorama import Fore
def startSession(db,User):
  while(True):
    print("Press 1 to add bills.")
    print("Press 2 to filer bills.")
    print("Press 3 to delete bills.")
    print("Press 4 to access bill panel. ")
    print("Press 5 to access report pannel.")
    print("Press 6 to access graph.")
    print("Press 7 to show some websites to gather further information about paying your bills.")
    print("Press 8 to change your password.")
    print("Press 9 to delete your account.")
    print("Press 0 to log out.")
    choice = int(input(">"))
    if(choice==1):
      ManageBills.createBill(db,User)
    elif (choice == 2):
      ManageBills.filterBill(db,User)
      
    elif (choice == 3):
      ManageBills.deleteBill(db,User)     
    elif (choice == 4):
      print("Press 1 to show all your bills, press 2 to show all your unpaid bill or press 3 to go back to the main menu. ")
      input12=int(input(">"))
      if input12==1:
        ManageBills.showmybills(db,User)
      elif input12==2:
        ManageBills.unpaid_bills(db,User)
      else:
        pass
    elif (choice == 5):
      print("\nWelcome to the report pannel!")
      print("Press 1 to get a daily report, for all the bills paid in the same day!")
      print("Press 2 to get a mothly report, for all the bills paid within a same month!")
      print("Press 3 to get a yearly report, for all the bills paid within a same year!\n")
      usr_input = int(input("Input: "))
      if usr_input == 1:
        print("Please give us the day you'd like a report of divided with / :")
        date = input(">")
        print("\n\nThe daily report of the", date, "is", Reports.showDailyReport(db,User,date))
      elif usr_input == 2:
        print("Give the month and year divded with / :")
        date = input(">")
        print("\n\nThe monthly report of the", date, "is", Reports.showMonthlyReport(db, User, date))
      elif usr_input == 3:
        print("Give the year: ")
        date = input(">")
        print("\n\nThe monthly report of the", date, "is", Reports.showYearlyReport(db, User, date))
      else:
        pass
    elif (choice == 6):
      CreateGraph(db,User)
      print("\n")
      input("Press Enter to continue...")
    elif(choice==7):
      paying()
    elif(choice == 8):
      Accounts.changePassword(db,User)
    elif(choice==9):
      Accounts.deleteAcc(db,User)
      return
    elif (choice == 0):
      return
    else:
      continue
def main():
  print(Fore.BLUE)
  print("          (         )            (               ")
  print(" (        )\ )   ( /(            )\ )         )  ")
  print(" )\ )    (()/(   )\())      (   (()/(      ( /(  ")
  print("(()/(     /(_)) ((_)\       )\   /(_))     )\()) ")
  print(" /(_))_  (_))     ((_)   _ ((_) (_))      ((_)\  ")
  print(Fore.RESET,end='')
  print(Fore.RED,end='')
  print("   / __| | _ \   / _ \  | | | | | _ \    | |  | ")
  print("  | (_ | |   /  | (_) | | |_| | |  _/    |_  _|  ")
  print("   \___| |_|_\   \___/   \___/  |_|        |_|   \n\n")
  print(Fore.RESET)
  db = Database(dbname="database")
  db.createtableifnotexists("All Bills", AllBills,AllBills.fromstring)
  db.createtableifnotexists("Accounts",Account,Account.fromstring)
  user = None
  while(True):
    now=True
    while now==True:
      try:
        print("Press 1 for Login\nPress 2 to register\nPress 3 for exiting")
        a=int(input())
        if a==1 or a==2 or a==3:
          now==False
      except Exception: 
          print("Please don't be a jerk.")
          continue
      
      if a==1:
        user=Login.CheckCredentials(db)
        if user==None:
          continue
          clear_screen.clear()  
        else:
          startSession(db,user)
          clear_screen.clear()  
      elif a==2:
        Accounts.createAcc(db)
      elif a==3:
        return
      else:
        continue
if __name__ == '__main__':
  main()