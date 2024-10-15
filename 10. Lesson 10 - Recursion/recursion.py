# rf => when a function calls itself

def add_one(num):
    if (num >= 9):
        return num + 1 # remvoing the retunn here cause somethin funny to occurr .. TEST THAT 
    
    total = num + 1
    print(total)

    return add_one(total) #recursive

mynewtotal = add_one(0)
print(mynewtotal)