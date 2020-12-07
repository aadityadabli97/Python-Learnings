list1=[["harry",1],["larry",2],["marie",3],["carry",4]]
for item in list1:
    print(item)
for item,lollypop in list1:
    print(item,lollypop)

dict1=dict(list1)

#for item,lollypop in dict1:
    #print(item,lollypop)   # yaha error dega islie .items() use karenge

for item,lollypop in dict1.items():
    print(item,lollypop)
for item in dict1:
    print(item) # yaha item print hoga

