user_inp = float(input("Please enter a number "))

calc = user_inp % 2

if calc == 0:
    print("The number", user_inp, "is even")
elif calc != 0:
    print("The number", user_inp, "is odd")
else:
    print("That is not a number!")