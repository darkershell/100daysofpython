import random

name = input("type the names: ")
list_names = name.split()
luck = random.randint(0, len(list_names))

print(f"how will pay the meal: {list_names[luck]}")
