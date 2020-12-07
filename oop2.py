
class Employee:
    no_of_leaves = 8
    pass

harry = Employee()       #creating harry object of Employee class
rohan = Employee()       #creating rohan object of Employee class

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 4554
rohan.role = "Student"

print(Employee.no_of_leaves)
print(Employee.__dict__)
Employee.no_of_leaves = 9
print(Employee.__dict__)
print(Employee.no_of_leaves)
"""yaha no_of_leaves class Employee ke andar hai to usko Employee use karke change kar sakte hai ,Employee ka ek instance
variable ban jaega joki dekhne ke lie Employee.__dict__ function use kar sakte hai isme Employee ka no_of_leaves naam ka
ek instance variable ban jaega jisme no_of_leaves ki value 9 ho jaegi matlab class ke andar  9 ho jaegi """

print(rohan.no_of_leaves)
print(rohan.__dict__)
rohan.no_of_leaves = 9
print(rohan.__dict__)
print(rohan.no_of_leaves)
"""yaha no_of_leaves class Employee ke andar hai to usko harry ya rohan se change nahi kar sakte , agar karenge bhi to 
wo change nahi hoga wo 8 hi aayega but rohan ka ek instance variable ban jaega joki dekhne ke lie rohan.__dict__ function
 use kar sakte hai isme rohan ka no_of_leaves naam ka ek instance variable ban jaega jisme no_of_leaves ki value 9 ho 
 jaegi but class ke andar wali no_of_leaves ki value change nahi hogi 8 hi rahegi """
