import matplotlib.pyplot as plt 
from database import Database
db = Database(dbname="database")
x=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#### ne vend to 123456789101112 ne dictionary vendosen totalet per cdo muaj.
one=db.getObjectsFrom("Gas Bill",lambda a:True)
two=db.getObjectsFrom("Monthly Bill",lambda a:True)
three=db.getObjectsFrom("Product Bill",lambda a:True)
four=db.getObjectsFrom("Random Bill",lambda a:True)

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
  else:
    dec.append(one[i][1])
for i in range (len(two)):
  if one[i][2]==1:
    jan.append(two[i][1])
  elif one[i][2]==2:
    feb.append(two[i][1])
  elif one[i][2]==3:
    mar.append(two[i][1])
  elif one[i][2]==4:
    apr.append(two[i][1])
  elif one[i][2]==5:
    may.append(two[i][1])
  elif one[i][2]==6:
    jun.append(two[i][1])
  elif one[i][2]==7:
    jul.append(two[i][1])
  elif one[i][2]==8:
    aug.append(two[i][1])
  elif one[i][2]==9:
    sep.append(two[i][1])
  elif one[i][2]==10:
    oct.append(two[i][1])
  elif one[i][2]==11:
    nov.append(two[i][1])
  else:
    dec.append(two[i][1])
for i in range (len(three)):
  if one[i][2]==1:
    jan.append(three[i][1])
  elif one[i][2]==2:
    feb.append(three[i][1])
  elif one[i][2]==3:
    mar.append(three[i][1])
  elif one[i][2]==4:
    apr.append(three[i][1])
  elif one[i][2]==5:
    may.append(three[i][1])
  elif one[i][2]==6:
    jun.append(three[i][1])
  elif one[i][2]==7:
    jul.append(three[i][1])
  elif one[i][2]==8:
    aug.append(three[i][1])
  elif one[i][2]==9:
    sep.append(three[i][1])
  elif one[i][2]==10:
    oct.append(three[i][1])
  elif one[i][2]==11:
    nov.append(three[i][1])
  else:
    dec.append(three[i][1])
for i in range (len(four)):
  if one[i][2]==1:
    jan.append(four[i][1])
  elif one[i][2]==2:
    feb.append(four[i][1])
  elif one[i][2]==3:
    mar.append(four[i][1])
  elif one[i][2]==4:
    apr.append(four[i][1])
  elif one[i][2]==5:
    may.append(four[i][1])
  elif one[i][2]==6:
    jun.append(four[i][1])
  elif one[i][2]==7:
    jul.append(four[i][1])
  elif one[i][2]==8:
    aug.append(four[i][1])
  elif one[i][2]==9:
    sep.append(four[i][1])
  elif one[i][2]==10:
    oct.append(four[i][1])
  elif one[i][2]==11:
    nov.append(four[i][1])
  else:
    dec.append(four[i][1])

exp={"total_jan":sum(jan),"total_feb":sum(feb),"total_mar":sum(mar), "total_apr":sum(apr), "total_may":sum(may),"total_jun":sum(jun),"total_jul":sum(jul),"total_aug":sum(aug),"total_sep":sum(sep),"total_oct":sum(oct),"total_nov":sum(nov),"total_dec":sum(dec)}
y = [exp["total_jan"],exp["total_feb"],exp["total_mar"],exp["total_apr"],exp["total_may"],exp["total_jun"],exp["total_jul"],exp["total_aug"],exp["total_sep"],exp["total_oct"],exp["total_nov"],exp["total_dec"]]
plt.plot(x, y) 
plt.xlabel('') 
plt.ylabel('') 
plt.title('Your expenses accross the months.') 
plt.show(block=False) 