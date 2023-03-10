# For Statements

# Initiate and iterate a list using for loop
words = ['cat', 'bird', 'horse']

for w in words:
    print(w, len(w))


# Initiate and iterate a dictionary using for loop
# Dictionary - a set of key and value pairs enclosed with a pair of braces {}
users = {'Rey': 'Inactive', 'Jayson': 'Active', 'Ervin': 'Active'}

for name, status in users.items():
    print(name, status)