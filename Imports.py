import math


math.sqrt(16)

#importing specific functions from a module 
from math import sqrt,pi
sqrt(25)
print(pi)   

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)


# Import with alias
import pandas as pd
df = pd.DataFrame(data)