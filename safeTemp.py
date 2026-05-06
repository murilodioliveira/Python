while True:
    scale = input("Enter C or F to indicate Celsius or Fahrenheit: ")
    if scale != 'C' and scale != 'F':
        print("Enter C or F for the scale!")
    else:
        while True:
            if scale == 'C':
                degrees = input("Enter the number of degrees: ")
                try:
                   int_degrees = int(degrees) 
                except ValueError:
                    print("Enter a valid number")
                    degrees = input("Enter the number of degrees: ")
                else:                    
                    if int_degrees >= 16 and int_degrees <= 38:
                        print("Safe")
                        break
                    else:
                        print("Dangerous")
                        break
            else:
                degrees = input("Enter the number of degrees: ")
                try:
                    float_degrees = float(degrees)
                except ValueError:
                    print("Enter a valid number")
                    degrees = input("Enter the number of degrees: ")
                else:
                    if float_degrees >= 60.8 and float_degrees <= 100.4:
                        print("Safe")
                        break
                    else:
                        print("Dangerous")
                        break
        break

"""             else:
                print("Enter a valid number") """