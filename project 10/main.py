# Build a Calculator

from calculator_module import logo

def additon(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

def remainder(num1, num2):
    quotient = num1 // num2
    final_value = num1 //(num2 * quotient)
    return final_value

def quotient(num1, num2):
    return num1 // num2

def percentage(num1, num2):
    final_value = round((num1 /num2) * 100, 2)
    return final_value


operations = {
    "+": additon,
    "-": subtraction,
    "*": multiplication,
    "/": division,
    "r": remainder,
    "p": percentage,
    
}


def calculator():
    """It's a basic calculator\n
    which perform additon, subtraction, multiplication and division and more."""
    
    print(logo)
    num1 = float(input("What is first number: "))
    
    operation_left = True
    while operation_left:
        for operator in operations:
            print(f"'{operator}' ", end=" ")
        
        op = input("Choose from this operators\n")
        num2 = float(input("What is second number: "))

        cal_func = operations[op]

        if cal_func == division or remainder or quotient:
            if num2 == 0:
                print("ZeroDivisionError")
                return 
            else:
                result = cal_func(num1, num2)
        else:
            result = cal_func(num1, num2)
        
        print(f"{num1} {op} {num2} = {result}")

        go_on = input(f"type 'y'  for continue with {result} or 'n' for a new calculation, to exit type 'e'\n").lower()
        if go_on == 'y':
            num1 = result
        elif go_on == 'n':
            calculator()
        else:
            operation_left = False




calculator()






