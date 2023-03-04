# For Statements

words = ['cat', 'bird', 'horse']

for w in words:
    print(w, len(w))


users = {'Rey': 'Inactive', 'Jayson': 'Active', 'Ervin': 'Active'}

for name, status in users.items():
    print(name, status)