import random


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
        print(" " * (qty - 1), end="")
        for leaf in range(row_num*2+1):
            test = random.randint(1, 4)
            if leaf == (row_num*2+1):
                if test == 1:
                    print("o")
                else:
                    print("^")
            elif leaf == (row_num*2):
                if test == 1:
                    print("o")
                else:
                    print("^")
            else:
                if test == 1:
                    print("o",end="")
                else:
                    print("^",end="")
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
