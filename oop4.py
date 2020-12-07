class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname                   # yaha self.name wala name instance variable hai jabki aname argument hai
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves


harry = Employee("Harry", 255, "Instructor")
rohan=Employee("Rohan",455,"student")

harry.change_leaves(34)  # class method use karke mai object se bhi class ke andar ki value change kar sakta hu jo abhi
# tak nahi kar pa raha tha  or  Employee.change_leaves se to kar hi sakta hu change  to ye fayda hai classmethod ka ye
# class attribute ko change kar raha hai instance variable ke attribute ko change nahi kar raha to agar rohan ya harry
# kisi se bhi access karo value 34 aayegi


print(harry.no_of_leaves)
print(Employee.no_of_leaves)          # to test whether class variable value gets changed or not
