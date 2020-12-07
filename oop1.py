# Classes - Template
# Object - Instance Of the Class

# DRY - Do not repeat Yourself

# get_no_of_films(table)


class Student:           # class me kuch na kuch hona chahiye likha hua or agar kuch nahi likh rahe to pass likh do
    pass


harry = Student()       # student class ka object
larry = Student()       # student class ka object

harry.name = "Harry"    #oject harry ke sath attribute name use kara
harry.std = 12
harry.section = 1
larry.std = 9
larry.subjects = ["hindi", "physics"]
print(harry.section, larry.subjects)  # yaha kuch bhi print karwa sakte hai list,integer,float value,double,tuples,
# dictionary etc..
