# Default Argument Values

# Create a function with 1 mandatory and 1 optional or default argument
def question(name, message='Do you love'):
    answer = input(f"{message} {name}?[Y/N]")

    if answer in ('Y', 'y'):
        print(f"Great! {name} is happy now!")
    elif answer in ('N', 'n'):
        print(f"Oh no! Sorry {name}!")
    else:
        print('Invalid response')

# Call defining function
question('Jayson')