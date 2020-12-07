#f=open("aadi2.text","a")       # ye ek nai file bana deta hai
#a=f.write(" harry bhai ")
#print(a)
#f.close()

# handle read and write both

f=open("aadi2.text ","r+")
print(f.read())
f.write("kyo")
print(f.read())

# f=open("aadi2.text","a")
# f.write(" here i am appending or adding my text ")