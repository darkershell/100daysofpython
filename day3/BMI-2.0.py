height = float(input("how tall are you?"))
weight = int(input("type your weight?"))

bmi = weight / (height * height)
pretty_bmi = "{:.2f}".format(bmi)

if bmi < 18.5:
    print(f"underweight range -- {pretty_bmi}")
elif bmi <= 24.9:
    print(f"Healthy Weight range -- {pretty_bmi}")
elif bmi <= 29.9:
    print(f"overweight range -- {pretty_bmi}")
else:
     print(f"obese range -- {pretty_bmi}")
