name = 'Atibila' #globally scoped, can be accessed anywhere

def greeting_a():
    color = "Black" #local scope, cannot be accessed outsied this function, can access any globally scoped items
    print(color)
    print(name) #prints Atibila

def greeting_b(firstname):
    color = "Red" #local scope, cannot be accessed outsied this function, can access any globally scoped items
    print(color)
    print(firstname) #prints whatever value is parsed in the function call => in this case ==> Anyeyure

def greeting_c(name):
    color = "Gold" #local scope, cannot be accessed outsied this function, can access any globally scoped items
    print(color)
    print(name) ##prints whatever value is parsed in the function call => in this case ==> Caleb

# you can even access globaly scoped methods in other methods
def another():
    greeting_c("Caleb")

# demostrating that locally scoped items can not be globally accessed.
# they can not be accessed in another function or method ither
# you cant access color(green) and method(special_greeting) outside greeting_d()
def greeting_d():
    color = "Green"
    def special_greeting(title):
        print(color)
        print(title)
    special_greeting("World Boss")

greeting_b("Anyeyure") #prints Anyeyure
print("")

another() #prints Caleb
print("")

greeting_d()
print()

# you cannot also locally modify any globally scoped items without using the 'global' keyword
color = 'purple'
count = 1

def modify_a():
    color = 'magenta'
    global count 
    count += 1
    print(count) # prints updated globally scoped count(1)
    print(color) # prints locally scoped color(magenta)

    def g_e(nomen):
        print(nomen)
    g_e('Oothur Pentdragon')

modify_a()
print("")
# applies to nested items with the same name but the keyword we use is nonlocal, this references the globall variable of the same name

def modify_b():
    color = 'magenta'
    global count 
    count += 1 #count will be 3 here... found this out my self when reading the code several times over
    print(count) # prints updated globally scoped count(1)
    print(color) # prints locally scoped color(magenta)

    def g_e(nomen):
        nonlocal color
        color = 'limited lime' # without this  a new variable called color will be created below
        print(color)
        print(nomen)
    g_e('Gandalf the Great')

modify_b()



