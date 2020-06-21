import matplotlib.pyplot as plt 
x=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
#### ne vend to 123456789101112 ne dictionary vendosen totalet per cdo muaj.
exp={"total_jan":1,"total_feb":2,"total_mar":3, "total_apr":4, "total_may":5,"total_jun":6,"total_jul":7,"total_aug":8,"total_sep":9,"total_oct":10,"total_nov":11,"total_dec":12}
y = [exp["total_jan"],exp["total_feb"],exp["total_mar"],exp["total_apr"],exp["total_may"],exp["total_jun"],exp["total_jul"],exp["total_aug"],exp["total_sep"],exp["total_oct"],exp["total_nov"],exp["total_dec"]]
plt.plot(x, y) 
plt.xlabel('') 
plt.ylabel('') 
plt.title('Your expenses accross the months.') 
plt.show(block=False) 