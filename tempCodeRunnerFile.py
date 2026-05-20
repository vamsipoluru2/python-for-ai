
# Read from environment
api_key = os.environ.get('API_KEY')
database = os.environ.get('DATABASE_NAME', 'default.db')

print(f"Using api_key: {api_key}")
print(f"Using database: {database}")