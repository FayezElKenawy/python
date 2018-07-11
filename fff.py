class Person:
    
    def __init__(self, first, last):
        self.firstname = first
        self.lastname = last



class Employee(Person):

    def __init__(self, first, last, staffnum):
        Person.__init__(self,first, last)
        self.staffnumber = staffnum



x = Person("Marge", "Simpson")
y = Employee("Homer", "Simpson", "1007")

print(y.firstname)
print(y.GetEmployee)