#---PYTHON-CALCULATOR-V2---
print("                            ---PYTHON-CALCULATOR-V2---                     ")

first_number = float(input("Enter the first number:"))
operation = input("Enter the operation:")
second_number = float(input("Enter the second number:"))

if operation == "+":
    print("The sum is", first_number + second_number)
elif operation == "-":
    print("The subtraction is", first_number - second_number)
elif operation == "*" or operation == "x":
    print("The multiplication is", first_number * second_number)
elif operation == "/":
    print("The division is", first_number / second_number)
elif operation == "%":
    print("The percentage is", (first_number % second_number) / 100)
else:
    print("It is not a mathematical operation")

repeat = input("¿Do you wish to perform another operation? (yes/no):")

while repeat != "no":
    first_number = float(input("Enter the first number:"))
    operation = input("Enter the operation:")
    second_number = float(input("Enter the second number:"))
    
    if operation == "+":
        
        print("The sum is", first_number + second_number)
    elif operation == "-":
        print("The subtraction is", first_number - second_number)
    elif operation == "*" or operation == "x":
        print("The multiplication is", first_number * second_number)
    elif operation == "/":
        print("The division is", first_number / second_number)
    elif operation == "%":
        print("The percentage is", (first_number % second_number) / 100)
    else:
        print("It is not a mathematical operation")
    
    repeat = input("¿Do you wish to perform another operation? (yes/no):")

    
    
