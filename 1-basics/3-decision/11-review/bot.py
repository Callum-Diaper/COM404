user_inp = str(input("So you've pulled the entire dungeon and you're being hit, do you want to use Hallowed Ground? "))
if user_inp == "is it worth it?":
    print("Maybe! We'll see with this handy program.")
    in_pull = str(input("So are you currently in the middle of a massive group of mobs? "))
    if in_pull == "yes":
        enemies_inp = str(input("Ok is there a lot of enemies? "))
        healer_inp = str(input("Do you trust your healer? "))

        if (enemies_inp == "yes") and (healer_inp == "no"):
            print("Use Hallowed before you die. Also pull less")

        elif (enemies_inp == "no") and (healer_inp == "yes"):
            print("You..you can pull more mate.")
    elif in_pull == "no":
        print("Go pull some mobs maybe? Its kind of your job")

elif user_inp == "nah":
    print("Good luck and be nice to your healer")

else:
    print("¯\_(ツ)_/¯")
