#Write a python program to create a basic calculator.

def main():
    print("=====MENU=====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Floor Division")
    print("=" * 15)
    print()
    choiceInput()


def choiceInput():
    print("=" * 15)
    choice = int(input("ENTER YOUR CHOICE:: "))
    a = float(input("ENTER FIRST NUMBER:: "))
    b = float(input("ENTER SECOND NUMBER:: "))
    if choice == 1:
        add(a, b)
    elif choice == 2:
        sub(a, b)
    elif choice == 3:
        mul(a, b)
    elif choice == 4:
        div(a, b)
    elif choice == 5:
        flDiv(a, b)
    else:
        print("WRONG INPUT!")
        main()


def add(a, b):
    result = a + b
    print(f"THE RESULT:: {result}")


def sub(a, b):
    result = a + b
    print(f"THE RESULT:: {result}")


def mul(a, b):
    result = a + b
    print(f"THE RESULT:: {result}")


def div(a, b):
    result = a + b
    print(f"THE RESULT:: {result}")


def flDiv(a, b):
    result = a + b
    print(f"THE RESULT:: {result}")

