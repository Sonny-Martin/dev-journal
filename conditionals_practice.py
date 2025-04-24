# Positive or Negative
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")



# Grade Checker
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")



# Odd or Even
score = int(input("Enter a score (1-100): "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")