user_name = str(input("What is your name? "))
age = int(input("How old are you? "))
weight = float(input("How much do you weigh in kilograms? "))
height = float(input("How tall are you in meters? "))

BMI = weight/(height*height)
print(user_name, "You are", age, "years old and your BMI is", BMI)