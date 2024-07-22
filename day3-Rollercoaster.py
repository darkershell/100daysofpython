print("RoolerCoaster")
height = int(input("how tall area you in cm ?"))
bill = 0

if height >= 120:
    age = int(input("How old are you ?"))
    if age < 12:
        bill = 5
        print(f"Child tickets are :{bill} ")
    elif age <= 18:
       bill = 7
       print(f"Youth tickets are : {bill} ")
    else:
        bill = 12
        print(f"Adult tickets are :{bill} ")
    
    wants_photo = input("do you want a photo taken Y or  N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is {bill}")

else:
    print("Sorry, you have to grow taller before you can ride")
