num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
operator = input("Enter operator (+, -, *, /): ")
if operator == "+":
    print("Result= ", num1 + num2)
elif operator == "-":
    print("Result= ", num1 - num2)
elif operator == "*":
    print("Result= ", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result= ", num1 / num2)
else:
    print("error!!!!!! Please division by zero")
