# concept of super() function and overriding
class A:
    classvar1 = "I am a class variable in class A"
    def __init__(self):
        self.var1 = "I am inside class A's constructor"
        self.classvar1 = "Instance var in class A"
        self.special = "Special"

class B(A):
    classvar1 = "I am in class B"

    def __init__(self):
        self.var1 = "I am inside class B's constructor"
        self.classvar1 = "Instance var in class B"
        # super().__init__()          # now we can use class A again if we want to using this super().__init__() function
        # print(super().classvar1)  agar isko uncomment karde to class a ke variable print ho jaenge b.var1 or
#b.classvar1 me


a = A()
b = B()

print(b.special, b.var1, b.classvar1)

"""ek bar jab function ya variable override ho jate hai to jo nayi value se override kara hai vo hi print hoti hai 
kya hota hai ki jab class A ki methods or variables ko override kar dete hai class B me uske bad class A ke method or 
or variable ki value print nahi karwa sakte becoz wo override ho chuke hai manlo classs a ka constructor chalana hai 
to nahi chala paenge apan but khujli hai class a ka constructor chalane ki to fir apne pass ek method hai uske liye 
usko kehte hai super().__init__() isse kya hoga ab class a ka constructor bhi chala paenge and variable ko access kar
paenge class A ke  . """