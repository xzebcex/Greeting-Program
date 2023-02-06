# This Program greet's the user with hello and ask for our name.

print("Hello!")

name = input("What is your name > ")  # ask for our name.
print(f"It's lovely meeting you,  {name}!")

age = input(f"How old are you {name}?\n")  # ask for our age.
print(f"You will be {str(int(age) + 1)} in a year.")
