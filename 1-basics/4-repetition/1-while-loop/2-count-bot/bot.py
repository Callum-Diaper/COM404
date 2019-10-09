user_inp =  int(input("How many live cables should I avoid? "))
cables_avoided = 0

while (cables_avoided < user_inp):
    cables_avoided = cables_avoided + 1
    print("Avoiding...Done!",cables_avoided,"live cables avoided")


print("All live cables have been avoided")