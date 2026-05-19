# Without classes - data and functions separate
name = "OpenAI"
model = "gpt-4o-mini"

def generate_response(prompt):
    # Process prompt...
    return response

# With classes - everything bundled together
class OpenAIClient:
    def __init__(self, name, model):
        self.name = name
        self.model = model
    
    def generate_response(self, prompt):
        # Process prompt...
        return response
    
# Why use classes?
# Classes help you write more understandable programs as they grow. Here’s the typical progression of a Python developer:
# 1. Single file scripts

# everything.py - All code in one file
api_key = "sk-..."
prompt = "Explain Python"
response = make_api_call(api_key, prompt)
print(response)                      

# oop

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color


# Create dog objects - using positional arguments
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Beagle")

# Or with named arguments (clearer)
dog3 = Dog(name="Charlie", breed="Poodle")

print(dog1.name)   # Buddy
print(dog2.breed)  # Beagle

# The __init__ method runs when you create a new object:
# self refers to the current object. It’s how an object keeps track of its own data:

