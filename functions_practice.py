def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(greet("Sonny"))
print(add(5, 7))
print(check_even_odd(10))
print(celsius_to_fahrenheit(25))
