import re
def check(email):
  regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
  if(re.search(regex,email)):  return True
  else:  return False
def check1(number):
  regex = '^[7-9]+[0-9]{7}$'
  if(re.search(regex,number)):  return True    
  else:  return False
