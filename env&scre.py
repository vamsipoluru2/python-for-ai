# Never put secrets in your code
# When working with APIs or databases, you’ll need:
# API keys
# Passwords
# Connection strings

import os
from dotenv import load_dotenv
# Load environment variables from .env file

# point to the .env file
load_dotenv("folder/.env")

# Read from environment
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_NAME', 'default.db')

print(f"Using api_key: {api_key}")
print(f"Using database: {database}")