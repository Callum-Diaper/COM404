user_inp = str(input("What kind of book is Beep reading? "))

if user_inp == "adventure":
    print("I like adventure books!")

elif user_inp == "fantasy":
    print("I like fantasy books!")

elif user_inp == "romance":
    print("I like romance books!")

else:
    print("I like",user_inp, "books!")

print("Finished reading the book")