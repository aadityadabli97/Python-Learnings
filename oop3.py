
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname                   # yaha self.name wala name instance variable hai jabki aname argument hai
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"


harry = Employee("Harry", 255, "Instructor")  #yaha se harry jaega self me aname me "Harry " jaega ,asalary me 255 jaega
# ,arole me "Instructor" jaega  , ye argument hamesha init function ko jata hai becoz ye constructor hai
# rohan = Employee()        #self ke andar harry ya rohan object jaega jo apan bhejna chahte hai
# harry.name = "Harry"
# harry.salary = 455
# harry.role = "Instructor"

# rohan.name = "Rohan"
# rohan.salary = 4554
# rohan.role = "Student"
print(harry.printdetails())  # iska matlab printdetails function ke andar harry chala gaya ab harry=self ho gaya to
# harry ki values print ho jaegi printdetails function me iska matlab self class ke object ko le leta hai

print(harry.salary)

