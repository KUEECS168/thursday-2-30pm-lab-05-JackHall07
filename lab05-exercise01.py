'''
Author: Jack Halligan
KUID: 3195571
Date: 3/6/26
Lab: lab02
Last modified: 3/7/26
Purpose: Exercise 1 Lab 5
'''

shopping_list = []

while True:
    print("Welcome to your Shopping List!")
    print("1) Add item")
    print("2) Check off item")
    print("3) Print list")
    print("4) Exit")

    choice = int(input("Enter a choice: "))

    if choice == 1:
        item = input("What else do you want?: ")
        shopping_list.append(item)

    elif choice == 2:
        index = int(input("Which item do you want to check off?: "))
        index = index - 1
        item = shopping_list[index]

        if len(item) > 2:
            middle = "-" * (len(item) - 2)
            new_item = item[0] + middle + item[-1]
        else:
            new_item = item
        shopping_list[index] = new_item

    elif choice == 3:
        print("Printing list...:")
        for i in range(len(shopping_list)):
            print(str(i + 1) + ") " + shopping_list[i])

    elif choice == 4:
        print("Alright then, goodbye!")
        break
