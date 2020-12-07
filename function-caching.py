# Function Caching In Python

import time
from functools import lru_cache       # functools ek module hota hai ,lru_cache ek decorator hota hai

@lru_cache(maxsize=32)                # ye function caching karta hai taki ek bar 3 second me khulne ke bad doosri bar
# turant call ho jae function time na le  ye decorator save kar lega us value ko,maxsize bata raha hai kitni value tak
# vo cache bana sakta hai jitna jada value denge utni memory khaega
def some_work(n):
    #Some task taking n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)                              # yaha 3 seconds lega
    some_work(1)                              # yaha 1 second lega
    some_work(6)                              # yaha 6 second lega
    some_work(2)                              # yaha 2 second lega
    print("Done... Calling again")
    input()                                   # yaha input lega or fir turant called again print kar dega 3 second nahi
    # lega fir kyoki function caching ho chuki hai
    some_work(3)
    print("Called again")

# yaha agar maxsize=3 hai to pichli 3 latest values ko hi cache karega jaise some_work(1),some_work(6),some_work(9) or
# uske bad 3 seconds delay karega agar mai chahta hu 3 seconds delay na kare to muje maxsize ki value badani padegi
# ab agar maxsize 32 kar diya to vo 32 value store karne ki shamta rakhega to 1 ,6,9 to mil hi jaegi usko to agli bar 3 ke
# liye wait nahi karna padega