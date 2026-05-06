def is_a_number(string):
    number = string
    try:
        number = int(string)
    except ValueError:
        check = False
        print("Is not a Integer!")
        return number, check
    else:
        check = True
        return number, check


def leaves(qty):
    for row_num in range(qty):
        print(" " * (qty - 1) + ("^" * (row_num * 2 + 1)))
        qty -= 1
def trunk(qty):
    for row_num in range(2):
        print(" " * (qty - 1) + ("#"))

treeSize = input("Enter the tree size: ")
treeSize, check = is_a_number(treeSize)
while True:
    if check:
        leaves(treeSize)
        trunk(treeSize)
        break
    else:
        continue
