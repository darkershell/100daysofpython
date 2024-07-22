print("thank you for choosing Python Pizza Deliveries!")
size = input("what size pizza do you want? S, M or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese Y or N: ")
pizza = 0


if size == "S":
    pizza += 15
elif size == "M":
    pizza += 20
else: 
    pizza += 25

if add_pepperoni == "Y":
    if size == "S":
        pizza += 2
    else:
        pizza += 3

if extra_cheese == "Y":
    pizza += 1

print(f"thank you for choosing Python Pizza, you final bill is: £{pizza}")
