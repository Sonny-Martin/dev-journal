def analyze_number(num):
    if num > 0:
        return "Positive number"
    elif num < 0:
        return "Negative number"
    else:
        return "Zero"
    
user_input = input("Enter a number: ")

try:
    number = float(user_input)
    result = analyze_number(number)
    print("Result:", result)
except ValueError:
    print("Thst wasn't a valid number! ")