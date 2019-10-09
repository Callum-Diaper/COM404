user_inp = int(input("Please enter a number "))
iterations = user_inp - 1 
total = user_inp

while iterations > 0:
    total = (total * iterations)
    iterations = iterations - 1
    
    
print("The factorial is",total)
