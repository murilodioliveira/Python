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
    scale = input("Enter C or F to indicate Celsius or Fahrenheit: ")
    if scale != 'C' and scale != 'F':
        print("Enter C or F for the scale!")
    else:
        while True:
            if scale == 'C':
                degrees = input("Enter the number of degrees: ")
                degrees, check = isANumber(degrees)
                if check and degrees >= 16 and degrees <= 38:
                        print("Safe")
                        break
                else:
                    print("Dangerous")
                    break
            else:
                degrees = input("Enter the number of degrees: ")
                degrees, check = isANumber(degrees)
                if check and degrees >= 60.8 and degrees <= 100.4:
                    print("Safe")
                    break
                else:
                    print("Dangerous")
                    break
        break

"""             else:
                print("Enter a valid number") """