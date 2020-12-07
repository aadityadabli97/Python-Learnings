# concept of public,protected and private
class Employee:
    no_of_leaves = 8
    var = 8
    _protec = 9       # protected variable defined it can be used or accessed  in only parent and child classes of parent
    __pr = 98         # private variable defined it can be used in only parent class or accessible in parent class only

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

    @classmethod
    def change_leaves(cls, newleaves):
        cls.no_of_leaves = newleaves

    @classmethod
    def from_dash(cls, string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good " + string)

emp = Employee("harry", 343, "Programmer")
print(emp._Employee__pr)         # to access private variable this term is used _Employee is written so that we dont
# mistakenly use it by another class name,and it is also easy to understand,simply it will throw error
print(emp._protec)    # to access protected variable this term is used