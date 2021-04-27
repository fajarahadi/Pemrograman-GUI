from Person import Person

class Student(Person) :
   def __init__(self, fname, mname, lname):
    super().__init__(fname, mname, lname)