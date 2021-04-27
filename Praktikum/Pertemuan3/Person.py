class Person:
  def __init__(self, fname,mname, lname):
    self.firstname = fname
    self.middlename = mname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.middlename, self.lastname)