user_inp = int(input("How many numbers should I sum up? "))
iterations = 0
total = 0

while (iterations < user_inp):
    iterations = iterations + 1
    print("Please enter number",iterations,"of",user_inp)
    add = int(input(""))
    total = total + add

print("The answer is",total)