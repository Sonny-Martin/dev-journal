# 1. Positive, Negative, or Zero
# This section checks if a number is positive, negative, or zero.
number = int(input("Enter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 2. Even or Odd Checker
# This checks whether a number is divisible by 2 (even) or not (odd).
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 3. Grade Checker
# This checks what letter grade a score between 1-100 falls into.
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
