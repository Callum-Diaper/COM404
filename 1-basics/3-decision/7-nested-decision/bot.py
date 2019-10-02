user_inp = str(input("What type of cover does the book have? "))

if user_inp == "soft":
    book_inp = str(input("Is the book perfect bound? "))
    if book_inp == "yes":
        print("Soft cover, perfect bound books are very popular!")
    else:
        print("Soft covers with coils or stitches are great for short books")
else:
    print("Books with hard covers can be more expensive!")
