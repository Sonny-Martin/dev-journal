def is_positive(num):
    if num > 0:
        return "Positive"
    elif num == 0:
        return "Zero"
    else:
        return "Negative"
    
print(is_positive(10))
print(is_positive(1))
print(is_positive(0))
print(is_positive(-5))

def get_larger_number(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return "both numbers are equal"
    
print(get_larger_number(10, 5))
print(get_larger_number(4, 9))
print(get_larger_number(3, 3))