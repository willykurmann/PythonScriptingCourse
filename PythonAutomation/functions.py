g = 100 # global variable

def print_data():
    "This is documentation string"
    print("This is testing world")

def addition(a,b=10): # Default arguments must be on the right of the required arguments
    "This is for addition"
    c = a+b # local variable
    print("Value of c is: {}".format(c))

def substraction(a,b):
    "This is for substracting 2 values"
    c = a-b
    return c

print_data()
z = substraction(100,40)
addition(z,z)

# required arguments
z = substraction(100,40) 
print(z)

# keyword arguments
z = substraction(b=40,  a=100) 
print(z)

# default arguments
addition(10) 
addition(10,20)