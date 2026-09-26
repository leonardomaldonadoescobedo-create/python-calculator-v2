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
    
menu()
menu2()
