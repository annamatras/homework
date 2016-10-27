
print("Welcome to Anna's calculator")

running = True
while running:
    print("1 = Addition")
    print("2 = Subtraction")
    print("3 = Multiplication")
    print("4 = Division")
    print("5 = Exit program")
    no = int(input("Enter number : "))
    if no == 1:
        print("Addition")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first + second
        print(first ,'+' ,second ,'=' , result)
    elif no == 2:
        print("Subtraction")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first - second
        print(first ,"-" ,second ,"=" , result)
    elif no == 3:
        print("Multiplication")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first * second
        print(first ,"*" ,second ,"=" , result)
    elif no == 4:
        print("Division")
        first = int(input("Enter first number :"))
        second = int(input("Enter second number :"))
        result = first / second
        print(first ,"/" ,second ,"=" , result)
    elif no == 5:
        print("Quit!")
        running = False
