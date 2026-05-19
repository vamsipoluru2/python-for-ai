
# Why use functions?
# Don’t repeat yourself: Write code once, use it many times
# Stay organized: Break complex programs into smaller pieces
# Fix bugs easier: Change code in one place, affects everywhere
# Test your code: Test each function separately

def greet():
    print("Hello, world!")
    print("Welcome to Python!")

# Call the function
greet()

#check_weather
def check_weather(temp):
    if temp > 30:
        print("It's hot outside!")
    elif temp < 10:
        print("It's cold outside!")
    else:
        print("The weather is nice!")

check_weather(35)  # Should print "It's hot outside!"

#parameters and arguments
def greet(first_name, last_name):
    print(f"Hello, {first_name} {last_name}!")

greet("Alice", "Smith")  # Should print "Hello, Alice Smith!"
#it will take in order of parameters


# Modifying global variables
# To change a global variable inside a function, use the global keyword:
counter = 0  # Global variable

def increment():
    global counter  # Declare we want to modify the global variable
    counter += 1

increment()
increment()
print(counter)  # 2


# Bad - using global variable
total = 0

def add_to_total(amount):
    global total
    total += amount

# Good - using parameters and return
def add_amounts(current_total, amount):
    return current_total + amount

total = 0
total = add_amounts(total, 10)
total = add_amounts(total, 20)
print(total)  # 30

#local variables
def calculate_area(radius):
    pi = 3.14  # Local variable
    area = pi * radius ** 2
    return area 
print(calculate_area(5))  # Should print the area of a circle with radius 5
# print(pi)  # This will cause an error because pi is not defined outside the function


#multiple parameters|

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

# Order matters!
calculate_total(100, 0.08, 10)  # $98





 #func with return value


 # This function only prints
def add_print(a, b):
    print(a + b)

# This function returns a value
def add_return(a, b):
    return a + b

# Now you can use the result
result = add_return(5, 3)
print(f"The result is {result}")  # The result is 8

def cal_area(width,height):
    area=width*height
    return area

print(cal_area(5,20))


#3

def get_greeting_print(name):
    print(f"Hello, {name}!")  # Just displays

def get_greeting_return(name):
    return f"Hello, {name}!"  # Gives back value

# Can't use print version's output
message = get_greeting_print("Alice")  # Prints but returns None
print(message)  # None

# Can use return version's output
message = get_greeting_return("Alice")  # Returns the string
print(message.upper())  # HELLO, ALICE!


