first_num = int(input("Please enter the first number "))
sec_num = int(input("Please enter the second number "))
third_num = int(input("Please enter the third number "))

odd_counter = 0
even_counter = 0

if first_num % 2 == 0:
    even_counter = even_counter + 1
elif first_num % 2 != 0:
    odd_counter = odd_counter + 1

if sec_num % 2 == 0:
    even_counter = even_counter + 1
elif sec_num % 2 != 0:
    odd_counter = odd_counter + 1

if third_num % 2 == 0:
    even_counter = even_counter + 1
elif third_num % 2 != 0:
    odd_counter = odd_counter + 1

print("There were", even_counter,"even numbers and", odd_counter, "odd numbers")