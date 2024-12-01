user_name = "AnwarulHoque"

def func():
    user_name = "Anwarul"
    # print(user_name)
    


# print(user_name)
func()

a = 99

# def func2(b):
#     c = a + b 
#     return c

# result = func2(2)
# print(result)

# def func3():
#     global a   # ----- don't use this global -----
#     a = 22

#  func3()
#  print(a)

def f1():
    a = 88
    def f2():
        print(a)
    return f2
myResult = f1()
myResult()

def anwarul(num):
    def actual(a):
        return a ** num
    return actual


f = anwarul(2)
g = anwarul(3)

print(f(3))
print(g(3))