
#project2
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? \n €"))
tip = float(input("what percentage tip would you like to give? 10, 12, or  15? \n"))
people = int (input("How many people to split the bill? \n"))

tip_perc = tip / 100
tip_perc_value = bill * tip_perc
final_bill = (bill + tip_perc_value) / people
pretty_bill = "{:.2f}".format(final_bill)
print(f"Each person should pay: €{pretty_bill}")


 #Life in Weeks.56
 # if we live until 90y old

process_age = ((90 - age) * 52)
age = int(input("how old are you?"))
print(f"You have {age} and you have more {process_age} weeks, enjoy!")



height = 1.8
score = 0
isWinning = True
#f-String
print(f"your score is {score},  your height is {height}, you are winning is {isWinning}")



#BMI calculation

weight = float(input ("your weight: "))
height = float(input ("your height: "))
bmi =  int(weight / height ** 2)
print (bmi)


# precedence order calculation
print(3 * 3 + 3 / 3 - 3) # 7
print(3 * (3 + 3) / 3 - 3) #3





## datas type exercise

number = input("Type the number:")
number1 = int(number[0])
number2 = int(number[1])
print(number1+number2)