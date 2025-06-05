# A simple function to greet someone by name
def greet(name):
    return f"Hello, {name}!"

# A function to add two numbers together
def add(a, b):
    return a + b

# This checks if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Convert Celsius temperature to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


# Calling and testing each function
print(greet("Sonny"))              # Should return "Hello, Sonny!"
print(add(5, 7))                   # 5 + 7 = 12
print(check_even_odd(10))         # 10 is even
print(celsius_to_fahrenheit(25))  # 25°C = 77°F
