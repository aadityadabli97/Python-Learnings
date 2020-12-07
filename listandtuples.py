# concept of list and tuples

"""grocery=["a","b","c","d","e",55] # mixed list
print(grocery)
print(grocery[4])     # accessing elements from list
print(grocery[1:])    # slicing in list returns a list
list ko slice karne se original list change nahi hoti list pe functions perform karne pe hoti hai
print(grocery[0:5:2])  # slice with step
print(grocery)
 a=[2,5,7,9,11,1]
print(a[0:]) # yaha jab slicing kari to original list aaayi
a.sort()   # ye function use karne se original list a change ho jaegi
print(a)
print(a[0:])  # yaha jab slice kara to sorted list aayi original nahi aayi
a.reverse()
print(a)
# to add element at last of list we use function
a.append(55)
print(a)
# to insert element anywhere at list we use function
a.insert(2,555)  # yaha 2 index hai jaha 555 insert hua
print(a)
a.remove(555)
print(a)
a.pop()  # ye last wala element hata dega 
print(a)"""

tp=(1,2,3)
#tp[1]=6    it shows that tuples are immutable
print(tp)
tp2=(1,)      # agar 1 element ka tuple banana hai to aise banega
print(tp2)
a=8
b=1
a,b=b,a    # swapping
print(a,b)