# Default Argument Values

# Create defining function
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