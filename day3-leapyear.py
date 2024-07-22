year = int(input("check year leap: "))


if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"It's Leap {year}")
        else:
            print(f"It's not leap {year}")
    else:
        print(f"It's Leap {year}")
else:
    print(f"It's not Leap {year}")
