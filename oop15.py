# concept of object introspection
class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.email = f"{fname}.{lname}@codewithharry.com"

    # def explain(self):
    #     return f"This employee is {self.fname} {self.lname}"
    #
    # @property
    # def email(self):
    #     if self.fname==None or self.lname == None:
    #         return "Email is not set. Please set it using setter"
    #     return f"{self.fname}.{self.lname}@codewithharry.com"
    #
    # @email.setter
    # def email(self, string):
    #     print("Setting now...")
    #     names = string.split("@")[0]
    #     self.fname = names.split(".")[0]
    #     self.lname = names.split(".")[1]
    #
    # @email.deleter
    # def email(self):
    #     self.fname = None
    #     self.lname = None


skillf = Employee("Skill", "F")
# print(skillf.email)
# o = "this is a string"
print(dir(skillf))                      #ye skillf ke sare function de dega or uske attributes bhi bata degaor jo usme
# defined hai wo bata dega
print(id("that that"))

# import inspect
# print(inspect.getmembers(skillf))


