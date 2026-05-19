
import requests

# Download a web page
response = requests.get("https://api.github.com")
print(response.status_code)  # Should print 200

print("Hello, World!")

# variables

name="Alice"
age=25
isstudent=True

First_name = "Alice"
FirstName = "Bob"

power=10**2
print(power)  # Should print 100

#strings
string="my name is Alice"
my_long_string = """This is a long string that spans multiple lines. 
                    It can contain "quotes" and 'apostrophes' without any issues."""


first_name = "Alice"
last_name = "Smith"
full_name = first_name + " " + last_name
print(full_name)  # Should print "Alice Smith"
long_dash="---"*10
print(long_dash)  # Should print a long line of dashes


#fstrings
name2 = "Alice"

string = f"hi there my name is {name2}"
# string2 = "hi there my name is {name}"

#loops
for i in range(5):
    print(i)  # Should print numbers from 0 to 4
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)  # Should print each number in the list   

# while loop
count = 0
while count < 5:
    print(count)  # Should print numbers from 0 to 4
    count += 1  

# data structures

#lists
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Should print 1

my_list=[1,"two",3.0,True]#can contain different data types
# list are ordered and mutable so accessed by index

print(my_list[1])#should print "two"
print(my_list[-1])  # Should print True

#list are mutable meaning we can change their content
my_list[0] = 10
print(my_list)  # Should print [10, 'two', 3.0, True]
my_list.insert(1,"new")#insert at index 1
print(my_list)  # Should print [10, 'new', 'two', 3.0, True]

#dictionaries
my_dict = {"name": "Alice", "age": 25, "is_student": True}
print(my_dict["name"])  # Should print "Alice"

my_dict["name"] = "Bob"
print(my_dict)  # Should print {'name': 'Bob', 'age': 25, 'is_student': True}

#tuples
my_tuple = (1, 2, 3)
print(my_tuple[0])  # Should print 1

colours = ("red", "green", "blue")
print(colours[1])  # Should print "green"

# sets
scores = [90, 85, 92,92]
unique_scores = set(scores)  # Convert to a set to get unique values
print(unique_scores)  # Should print {85, 90, 92}

numbers={1,2,3,4,5}
print(numbers)  # Should print {1, 2, 3, 4, 5}
