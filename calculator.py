#---PYTHON-CALCULATOR-V3---

def menu():
    
    print("=== PYTHON-CALCULATOR-V3 ===")
    print("")
    print("=== Basic Operations ===")
    
    options = [
        "1. Addition" ,
        "2. Subtraction" ,
        "3. Multiplication" ,
        "4. Division" , 
    ]
    
    for i in options:
        print(i)
    
def menu2():
    
    print("=== Other Operations ===")
    
    options = [
        "5. Percentage" ,
        "6. Power" ,
        "7. Modulo" ,
        "8. Square Root" , 
        "9. Factorial" ,
        "",
        "0. Exist" , 
    ]
    
    for i in options:
        print(i)
    
    print("========================")

def sum(a , b):
    return a + b
    
def subtraction(a , b):
    return a - b
    
def multiplication(a , b):
    return a * b

def division(a , b):
    try:
        return a / b
    except ZeroDivisionError:
        print("SYNTAX ERROR")
        
while True:
    menu()
    menu2()
    
    try:
        option = int(input("Write an option:"))
        
        if option == 0:
            break
        
        a = int(input("Write a first number:"))
        b = int(input("Write a second number:"))
        
        if option == 1:
            answer = sum(a , b)
            print("The answer is:" , answer)
        elif option == 2:
            answer = subtraction(a , b)
            print("The answer is:" , answer)
        elif option == 3:
            answer = multiplication(a , b)
            print("The answer is:" , answer)
        elif option == 4:
            answer = division(a , b)
            print("The answer is:" , answer)
        else:
            print("This options is in process")
        
    except ValueError:
        print("SYNTAX ERROR")
