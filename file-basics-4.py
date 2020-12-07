with open("aaditya.txt") as f:
# jaise hum file ko open or close karte hai f=open() or f=close() likhke uski jagah with keyword ko use karke file
# open kar sakte hai, iska ye fayda hai ki isme file  close karne ki jarwat nahi padegi f.close likhke kyoki with keyword
# usko apne aap handle karta hai
    a=f.read(4)
    print(a)