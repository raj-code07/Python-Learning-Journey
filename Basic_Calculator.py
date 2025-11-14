# Project Overview: Create a simple calculator that can perform basic arithmetic operations such as addition
#, subtraction, multiplication, and division. Each operation will be implemented as a separate function,
# and the user can choose which operation to perform. add(a, b) for addition subtract(a, b) for subtraction
# multiply(a, b) for multiplication divide(a, b) for division


def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if (b!=0):
        return a/b
    else:
        print("Error: division by zero")

def Calculator():
    print("Select operation:")
    print("1. Addition")
    print("2. subtraction")
    print("3. Multplication")
    print("4. division")

    choise= input("Enter choise (1/2/3/4):")

    try:
        num1=float(input("Enter first number:"))
        num2=float(input("Enter second number:"))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    if choise =='1':
        print("Result:", add(num1,num2))
    elif choise =='2':
        print("Result:",subtract(num2,num2))
    elif choise =='3':
        print("Result:",multiply(num2,num2))
    elif choise =='4':
        print("Result:",divide(num1,num2))
    else:
        print("Invalid choise!")

Calculator()