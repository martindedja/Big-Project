  '''
  @staticmethod
  def createclassBill(db,user):
  	ID = str(input("Enter bill ID: "))
  	total = str(input("Enter bill total: "))
  	date = str(input("Enter bill date: "))
  	month = str(input("Enter bill month: "))
  	year = str(input("Enter bill year: "))
  	status = str(input("Enter bill status: "))
  	type_ = str(input("Enter bill type: "))
  	product_name = str(input("Enter product name: "))
	class_input = "/".join[str(ID),str(total),str(date),str(month),str(year),str(status),str(type_),str(product_name),str(user)]
	cl1 = class_input.split("/")
    if len(cl1) == 8 and cl1[1].isdigit() and cl1[2] and cl1[3] and cl1[4]:
      if cl1[5] == 'not_paid' or 'paid':
        cl2 = AllBills(cl1[0],cl1[1],cl1[2],cl1[3],cl1[4],cl1[5],cl1[6],cl1[7],user)
        db.appendObjectInto("All Bills",cl2)
        print(Fore.GREEN)
        print("Bill added")
        print(Fore.RESET)
      else:
        print(Fore.RED)
        print("Bill status error! write not_paid or paid!!")
        print(Fore.RESET)
    else:
      print(Fore.RED)
      print("Wrong bill structure")
      print(Fore.RESET)
      '''