import matplotlib.pyplot as plt 
import colorama
from colorama import Fore
from colorama import init
from database import Database

def CreateGraph(db,username):
  x=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
  ones=db.getObjectsFrom("All Bills", lambda a: a.username == username)
  year = input("Enter the year you are looking for: ")
  jan=[]
  feb=[]
  mar=[]
  apr=[]
  may=[]
  jun=[]
  jul=[]
  aug=[]
  sep=[]
  oct=[]
  nov=[]
  dec=[]

  for bill in ones:
    if int(bill.month)==1 and int(year) == int(bill.year):
      jan.append(int(bill.total))
    elif int(bill.month)==2 and int(year) == int(bill.year):
      feb.append(int(bill.total))
    elif int(bill.month)==3 and int(year) == int(bill.year):
      mar.append(int(bill.total))
    elif int(bill.month)==4 and int(year) == int(bill.year):
      apr.append(int(bill.total))
    elif int(bill.month)==5 and int(year)  == int(bill.year):
      may.append(int(bill.total))
    elif int(bill.month)==6 and int(year)  == int(bill.year):
      jun.append(int(bill.total))
    elif int(bill.month)==7 and int(year)  == int(bill.year):
      jul.append(int(bill.total))
    elif int(bill.month)==8 and int(year) == int(bill.year):
      aug.append(int(bill.total))
    elif int(bill.month)==9 and int(year)  == int(bill.year):
      sep.append(int(bill.total))
    elif int(bill.month)==10 and int(year)  == int(bill.year):
      oct.append(int(bill.total))
    elif int(bill.month)==11 and int(year)  == int(bill.year):
      nov.append(int(bill.total))
    elif int(bill.month)==12 and int(year)  == int(bill.year):
      dec.append(int(bill.total))
    else:
      pass

  y=[sum(jan),sum(feb),sum(mar),sum(apr), sum(may),sum(jun),sum(jul),sum(aug),sum(sep),sum(oct),sum(nov),sum(dec)]
  plt.plot(x, y) 
  plt.xlabel('') 
  plt.ylabel('') 
  plt.title('Your expenses accross the months.')
  plt.show(block=False)
  
def paying():
  print(Fore.BLUE)
  print("\nHere are some sites that can help you gather further information to pay bills from certain sources:\n")
  print(Fore.RESET)
  print(Fore.GREEN)
  print("\nWater and Electricity ->",end="")
  print(Fore.RESET)
  print(Fore.LIGHTBLUE_EX)
  print("https://www.easypay.al/sherbimet/utilitetet/fatura-dritave-dhe-ujit/")
  print(Fore.RESET)
  print(Fore.GREEN)
  print("Digitalb -> ",end="") 
  print(Fore.RESET)
  print(Fore.LIGHTBLUE_EX)
  print("https://www.digitalb.al/ndihma/dyqanet-2/")
  print(Fore.RESET)
  print(Fore.GREEN)
  print("Tring -> ",end="")
  print(Fore.RESET)
  print(Fore.LIGHTBLUE_EX)
  print("https://www.tring.al/familjare/tring-shop/dyqanet-tring/")
  print(Fore.RESET)
  print(Fore.GREEN)
  print("Vodafone -> ",end="")
  print(Fore.RESET)
  print(Fore.LIGHTBLUE_EX)
  print("https://www.vodafone.al/store-locator/")
  print(Fore.RESET)
  print(Fore.GREEN)
  print("From the Government -> ",end="" )
  print(Fore.RESET)
  print(Fore.LIGHTBLUE_EX)
  print("https://e-albania.al/eAlbaniaServices/Packages.aspx?lvl=2&path_code=1118&cat_id=1118")
  print(Fore.RESET)
  print(Fore.GREEN)
  print("Telekom -> ",end=""  )
  print(Fore.RESET)
  print(Fore.LIGHTBLUE_EX)
  print("https://www.telekom.com.al/dyqane/")
  print(Fore.RESET)
  print(Fore.GREEN)
  print("Western Union,mainly for sending money -> ",end="")
  print(Fore.RESET)
  print(Fore.LIGHTBLUE_EX)
  print("https://www.westernunion.com/al/en/send-money.html")
  print(Fore.RESET)
  print(Fore.GREEN)
  print("A list of banks in Albania -> ",end="" )
  print(Fore.RESET)
  print(Fore.LIGHTBLUE_EX)
  print("https://sq.wikipedia.org/wiki/Lista_e_bankave_n%C3%AB_Shqip%C3%ABri")
  print(Fore.RESET)