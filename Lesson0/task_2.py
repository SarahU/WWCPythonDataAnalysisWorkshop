def get_input(nametype):
    return input(f"Please enter your {nametype}: ")

first_name = get_input("First Name")
last_name = get_input("Last Name")

print(f"Welcome {last_name}, {first_name}")