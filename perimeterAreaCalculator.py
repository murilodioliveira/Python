import inspect

def area(width, length):
    area = width * length
    return area
def perimeter(width, length):
    perimeter = (width * 2) + (length * 2)
    return perimeter
def isANumber(string):
    number = string
    try:
        number = int(string)
    except ValueError:
        check = False
        frame = inspect.currentframe().f_back
        varName = [name for name, val in frame.f_locals.items() if val is string]
        print(f"{varName} Is not a number!")
        return number, check
    else:
        check = True
        return number, check

while True:
    width = input("Enter the width for the rectangle: ")
    length = input("Enter the length for the rectangle: ")
    width, check = isANumber(width)
    #print(type(width))
    #print(check)
    if check:
        length, check = isANumber(length)
        #print(type(length))
        #print(check)
        if check:
            area = area(width, length)
            perimeter = perimeter(width, length)
            print(f"Area of the rectangle: {area}")
            print(f"Perimeter of the rectangle: {perimeter}")
            break
        else:
            continue
    else:
        continue