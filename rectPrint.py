rows = 0
rec = 'O'
while True:
    columns = input("Enter the with for the rectangle: ")
    if columns.isdigit():
        while rows < 5:
            print(rec *int(columns))
            rows += 1
        break
    else:
        print("Enter a number!")
    