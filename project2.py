
print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $\n"))
tip = float(input("what percentage tip would you like to give? 10, 12, or  15? \n"))
people = int (input("How many people to split the bill? \n"))
result  = (tip / bill) * 100.0
result_final = result / people
print(f"Each person should pay: {result_final}")




# #Life in Weeks.56
# # if we live until 90y old

# age = int(input("how old are you?"))
# process_age = ((90 - age) * 52)
# print(f"You have {age} and you have more {process_age} weeks, enjoy!")



# score = 0
# height = 1.8
# isWinning = True
# #f-String
# print(f"your score is {score},  your height is {height}, you are winning is {isWinning}")



# #BMI calculation

# weight = float(input ("your weight: "))
# height = float(input ("your height: "))
# bmi =  int(weight / height ** 2)
# print (bmi)


## precedence order calculation
# print(3 * 3 + 3 / 3 - 3) # 7
# print(3 * (3 + 3) / 3 - 3) #3





## datas type exercise

# number = input("Type the number:")
# number1 = int(number[0])
# number2 = int(number[1])
# print(number1+number2)80