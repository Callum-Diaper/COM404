user_inp = int(input("How many miles must I travel before I reach the secret base? "))
print("I will count the miles")

for i in range (user_inp, 1, -1):
    print("I have",user_inp,"miles to go before I reach the base.")
    user_inp = user_inp - 1

print("I have arrived at the secret headquarters of the MIB!")
print("Its time to sneak in.")

