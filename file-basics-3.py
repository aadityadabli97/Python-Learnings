f=open("aaditya.txt")
print(f.seek(0))   # f.seek function file pointer ko 15 position pe le jaega
print(f.tell())     # f.tell function bataega pointer ki position
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())