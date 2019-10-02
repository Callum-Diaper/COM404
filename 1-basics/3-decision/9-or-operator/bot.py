user_inp = str(input("What type of adventure should I have? "))

if (user_inp == "scary") or (user_inp == "short"):
    print("Entering the dark forrest!")
elif (user_inp == "safe") or (user_inp == "long"):
    print("Taking the safe route!")
else:
    print("Not sure which route to take.")
    