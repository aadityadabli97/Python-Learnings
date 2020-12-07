# Lambda functions or anonymous functions
# def add(a, b):
#     return a+b
#
# # minus = lambda x, y: x-y
#
# def minus(x, y):
#     return x-y
#
# print(minus(9, 4))


a = [[1, 14], [8, 6], [5, 23]]
b=a.copy()
a.sort(key=lambda x: x[0])
b.sort(key=lambda x: x[1])
print(a)
print(b)



