# i need to give more time to undesten better this yield function {42 - 51:30}

def even_generator(limit):
    for i in range(2, limit + 1 , 2):
        # print(i)
        # return i
        yield i
        
# print(even_generator(10))

for num in even_generator(10):
    print(num)
