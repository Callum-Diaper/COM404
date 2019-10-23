def item_from_suitcase(item_inp):
    if item_inp == "toothbrush":
        print("A toothbrush. Well, got to have clean teeth!")
    elif item_inp == "spidey suit":
        print("My Spidey suit! I won't be needing this. I am on holiday.")
    else:
        print("An unexpected item! It could be useful.")

item_inp = str(input("I wonder what's in my suitcase... "))
item_from_suitcase(item_inp)