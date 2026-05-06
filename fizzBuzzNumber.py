def isANumber(string):
    number = string
    try:
        number = float(string)
    except ValueError:
        check = False
        print("Is not a number!")
        return number, check
    else:
        check = True
        return number, check
while True:
    number = input("Enter an integer: ")
    number, check = isANumber(number)
    if check and ((number % 3 == 0) and (number % 5 == 0)):
        print("Fizz Buzz")
        break
    elif check and (number % 3 == 0):
        print("Fizz")
        break
    elif check and (number % 5 == 0):
        print("Buzz")
        break
    elif check == False:
        continue
    else:
        break