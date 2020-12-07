# concept of scope global variable and global keyword
l=10  # global variable
def func(n):
    global l
    l=l+45   # local variable
    m=8   # local variable
    print(l,m)
    print(n,"i have printed")
func("this is me ")

"""local variable matlab function ke andar define hota hai khud ka paisa global variable matlab bahar function ke 
sarkar ka paisa . agar local variable ko bahar call karoge to error aayegi kyoki vo function ke andar hi use ho sakta 
hai sirf family wo paisa use karegi par agar man lo local me koi variable m naam ka define nahi hai or function me to 
print(m) likh diya to global m ki value print kar dega  agar global m defined hai to yani apan sarkar ka paisa use 
kar sakte hai.agar apne ko local variable ki value change karna hai to apan kar sakte hai par function ke andar global 
variable ki value change nahi kar sakte.agar global variable ki value change karne ka bhot man hai function ke andar to 
kar sakte hai global keyword ka use karke """

l2=3
def func2():
    l2=l2+3
    print(l2)
func2()