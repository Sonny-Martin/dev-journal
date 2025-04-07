num1 = float(input("Enter first number: "))
operator = input("Choose an operation (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == '+':
    result = num1 + num2
elif operator == '-':
    result = num1 - num2
elif operator == '*':
    result = num1 * num2
elif operator == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "You can't divide by zero!"
else:
    result = "Invalid operator."

print("Result:", result)
