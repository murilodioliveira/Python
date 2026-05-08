def plus_one(number):
    return number + 1
def add(number1, number2):
    total_sum = number1
    for i in range(number2):
        total_sum = plus_one(total_sum)
    return total_sum
def multiply(number1, number2):
    total_mul = number1
    for i in range(number2-1):   
        total_mul = add(total_mul, number1)
    return total_mul
print(plus_one(5))

print(add(10,6))

print(multiply(9,9))
