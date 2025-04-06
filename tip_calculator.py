bill = float(input("what was the total bill? $"))
tip_percent = float(input("what percentage tip would you like to give? (e.g 15 for 15%) "))
people = int(input("how many people to split the bill? "))
tip = bill * (tip_percent / 100)
total = bill + tip
amount_per_person = total / people
print(f"each person should pay: ${round(amount_per_person, 2)}")