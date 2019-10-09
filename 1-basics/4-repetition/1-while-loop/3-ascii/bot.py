user_inp = int(input("How many bars should be charged? "))
bars_charged = 0


while (bars_charged < user_inp):
    bars_charged = bars_charged + 1
    battery_level = "█ "*bars_charged
    print("Charging:",battery_level)

print("The battery is fully charged")