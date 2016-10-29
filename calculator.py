import sys

print("Welcome to Anna's calculator.\nLet's do some math!")
print("")  # left line before running


# define functions
def add(x, y):
    """This function adds two numbers"""
    return str(int(x) + int(y))  # change string into integer


def subtract(x, y):
    """This function subtracts two numbers"""
    return str(int(x) - int(y))


def multiply(x, y):
    """This function multiplies two numbers"""
    return str(int(x) * int(y))


def divide(x, y):
    """This function divides two numbers"""
    return str(int(x) / int(y))

while True:

    num1 = input("Enter first number (or a letter to exit)")
    if num1.isalpha():
        print("Bye, bye!")
        exit()

    operation = input("Enter an operation (+,-,* or /): ")
    if operation == '+' or operation == '-' or operation == '*' or operation == '/':
        num2 = input("Enter second number: ")
        if operation == '+':
            print("Result: ", add(num1, num2))

        elif operation == '-':
            print("Result: ", subtract(num1, num2))

        elif operation == '*':
            print("Result: ", multiply(num1, num2))

        elif operation == '/':
            if num2 == "0":  # if sb decides to devide by 0
                print("Ooops! Dividing by 0 is illegal! Try again.")
            else:
                print("Result: ", divide(num1, num2))
    else:
        print("Are you sure?") # if sb enter wrong sign
        user_input = input("yes or no?: ")
        if user_input == 'yes':
            print("There is not an option!")
        elif user_input == 'no':
            print("Try again! Choose +,-,* or /")
        else:
            print("Maybe you should use a traditional calculator?")
            exit()
    print("")  # left line before next loop

