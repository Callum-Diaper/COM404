#I don't know what this program will be yet but imma just start writing stuff and figure it out later
char_name = str(input("What is your character's name "))
base_health = int(input("Please pick a random/generated number between 1 and 8 "))
con = int(input("Please enter your constitution modifier "))

calc = base_health+con
health = "♥"*calc

print(char_name,", your maximum HP at level 1 will be", health)
