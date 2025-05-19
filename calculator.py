def calculator():
    num1 = float(input("enter the first number:"))
    operator = input(" enter the operator (+,-,*,/):")
    num2 = float(input("enter the second number:"))
    if operator == "+":
        print(f"result: {num1 + num2} ")
    elif operator == "-":
        print(f"result: {num1 - num2} ")
    elif operator == "*":
        print(f"result: {num1 * num2} ")
    elif operator == "/":
        if num2 != 0:
            print(f"result: {num1 / num2} ")
        else:
            print("error: division by zero. ")
    else:
        print("invalid operator.")
calculator()
