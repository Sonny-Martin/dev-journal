# Ask the user to enter a number and store it as an integer
num = int(input("Enter a number: "))

# Check if the number is positive, negitive, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print(" The number is negitive.")
else:
    print("The number is zero.")

# Check if the number is divisible by both 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("It is divisible by both 3 and 5.")
else:
    print("It is not divisible by both 3 and 5.")

# Check if the number is a mulitiple of 7
if num % 7 == 0:
    print(" It is a muliple of 7.")
else:
    print("it is not a multiple of 7.")