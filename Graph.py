import matplotlib.pyplot as plt 
from database import Database
db = Database(dbname="database")
x=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#### ne vend to 123456789101112 ne dictionary vendosen totalet per cdo muaj.
one=db.getObjectsFrom("All Bills",lambda a:True)

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
for i in range (len(one)):
  if one[i][2]==1:
    jan.append(one[i][1])
  elif one[i][2]==2:
    feb.append(one[i][1])
  elif one[i][2]==3:
    mar.append(one[i][1])
  elif one[i][2]==4:
    apr.append(one[i][1])
  elif one[i][2]==5:
    may.append(one[i][1])
  elif one[i][2]==6:
    jun.append(one[i][1])
  elif one[i][2]==7:
    jul.append(one[i][1])
  elif one[i][2]==8:
    aug.append(one[i][1])
  elif one[i][2]==9:
    sep.append(one[i][1])
  elif one[i][2]==10:
    oct.append(one[i][1])
  elif one[i][2]==11:
    nov.append(one[i][1])
  elif one[i][2]==12:
    dec.append(one[i][1])
  else:
    print("You can't perform this action. No bills registered.")


exp={"total_jan":sum(jan),"total_feb":sum(feb),"total_mar":sum(mar), "total_apr":sum(apr), "total_may":sum(may),"total_jun":sum(jun),"total_jul":sum(jul),"total_aug":sum(aug),"total_sep":sum(sep),"total_oct":sum(oct),"total_nov":sum(nov),"total_dec":sum(dec)}
y = [exp["total_jan"],exp["total_feb"],exp["total_mar"],exp["total_apr"],exp["total_may"],exp["total_jun"],exp["total_jul"],exp["total_aug"],exp["total_sep"],exp["total_oct"],exp["total_nov"],exp["total_dec"]]
plt.plot(x, y) 
plt.xlabel('') 
plt.ylabel('') 
plt.title('Your expenses accross the months.') 
plt.show(block=False) 