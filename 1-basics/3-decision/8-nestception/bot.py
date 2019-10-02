user_inp = str(input("Where should I look? "))

if user_inp == "in the bedroom":
    bedroom_inp = str(input("Where should I look in the bedroom? "))
    if bedroom_inp == "under the bed":
        print("Found some shoes but no battery")
    else:
        print("Found some mess but no battery.")

elif user_inp == "in the bathroom":
    bath_inp = str(input("Where in the bathroom should I look? "))
    if bath_inp == "in the bathtub":
        print("Found a rubber duck but no battery")
    else:
        print("It is wet but I found no battery.")

elif user_inp == "in the lab":
    lab_inp = str(input("Where in the lab should I look? "))
    if lab_inp == "on the table":
        print("Yes! I found my battery!")
    else:
        print("Found some tools but no battery.")
else:
    print("I do not know where that is but I will keep looking.")