class Reports():

  @staticmethod
  def showDailyReport(db, username, date):
    total = 0
    bill_date = date.split("/")
    if bill_date[0].isdigit() and bill_date[1].isdigit() and bill_date[2].isdigit():
      all_user_bills = db.getObjectsFrom("All Bills", lambda x: x.username == username and int(x.date) == int(bill_date[0]) and int(x.month) == int(bill_date[1]) and int(x.year) == int(bill_date[2]))
      if len(all_user_bills) != 0:
        for bill in all_user_bills:
          total += int(bill.total)
        return total
      else:
        return "Error"
    else:
      print("Not a valid date!!!")

  @staticmethod
  def showMonthlyReport(db, username, date):
    total = 0
    for i in range(1,31):
      dt = "/".join([str(i),str(date)])
      daily_total = Reports.showDailyReport(db, username, dt)
      if daily_total != "Error":
        total += int(daily_total)
    return total
  
  @staticmethod
  def showYearlyReport(db, username, date):
    total = 0
    for i in range(1,13):
      dt = "/".join([str(i), str(date)])
      monthly_total = Reports.showMonthlyReport(db, username, dt)
      if monthly_total != "Error":
        total += int(monthly_total)
    return total