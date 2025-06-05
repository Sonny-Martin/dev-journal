# Check if a number is positive, zero, or negative
def is_positive(num):
    if num > 0:
        return "Positive"
    elif num == 0:
        return "Zero"
    else:
        return "Negative"

# Testing the function with different numbers
print(is_positive(10))   # Should return "Positive"
print(is_positive(1))    # Should return "Positive"
print(is_positive(0))    # Should return "Zero"
print(is_positive(-5))   # Should return "Negative"


# Check which number is bigger, or if they're the same
def get_larger_number(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "both numbers are equal"

# Testing with different pairs
print(get_larger_number(10, 5))  # 10 is bigger
print(get_larger_number(4, 9))   # 9 is bigger
print(get_larger_number(3, 3))   # Same numbers


# Check if a number is divisible by both 3 and 5
def is_divisible_by_3_and_5(num):
    if num % 3 == 0 and num % 5 == 0:
        return "Divisible by both"
    else:
        return "Not divisible by both"

# Testing the function
print(is_divisible_by_3_and_5(15))  # 15 is divisible by 3 and 5
print(is_divisible_by_3_and_5(10))  # Only divisible by 5
print(is_divisible_by_3_and_5(9))   # Only divisible by 3


# Check if a number is a multiple of 7
def is_multiple_of_7(num):
    if num % 7 == 0:
        return "Yes"
    else:
        return "No"

# Testing with different numbers
print(is_multiple_of_7(14))  # 14 is a multiple of 7
print(is_multiple_of_7(9))   # 9 is not a multiple of 7


# Find the absolute difference between two numbers
def absolute_difference(a, b):
    difference = a - b
    return abs(difference)

# Testing to make sure it works no matter the order
print(absolute_difference(10, 4))   # Difference is 6
print(absolute_difference(4, 10))   # Still 6

