for i in range(5):
    print("Loop number", i)

for number in range(1, 11):
    print(number)

    for number in range(2,21,2):
        print(number)

for number in range(1, 21):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
