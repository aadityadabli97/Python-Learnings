# file i/o basics
"""
"r" = open file for reading  //default mode
"w"=open a file for writing
"x"=creates file if not exists
"a"=add more content to the file
"t"=text mode   //default mode
"b"=binary mode
"+"=read and write
"""

f=open("aaditya.txt")
content=f.read()
print(content)
#-----------------------------------------------------------------------------------

f=open("aaditya.txt","r")       # agar yaha r bhi likhe to same aayega
content=f.read()
print(content)

# default rt(read text) hota hai rb(read binary) nahi
f=open("aaditya.txt","rt")
content=f.read()
print(content)
#------------------------------------------------------------------------------------
f=open("aaditya.txt")
print(f.readline()) # ye line by line read karta hai
print(f.readlines())
content=f.read(5)
print(content)

content=f.read(3)
print(content)
f.close()

