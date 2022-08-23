# Reworked calculator

answer = input("Hi! Would you like to solve a math problem? yes/no: ")

if answer.lower() == "yes":
    number_one = input("Type a number: ")
    math_symbol = input("Type the mathematic operator you want to use: ")
    number_two = input("Type a number: ")
    if math_symbol == "+":
        print(number_one, math_symbol, number_two, "=", float(number_one) + float(number_two))
    elif math_symbol == "-":
        print(number_one, math_symbol, number_two, "=", float(number_one) - float(number_two))
    elif math_symbol == "*":
        print(number_one, math_symbol, number_two, "=", float(number_one) * float(number_two))
    elif math_symbol == "/":
        print(number_one, math_symbol, number_two, "=", float(number_one) / float(number_two))
    elif math_symbol == "%":
        print(number_one, math_symbol, number_two, "=", float(number_one) % float(number_two))
    elif math_symbol == "**":
        print(number_one, math_symbol, number_two, "=", float(number_one) ** float(number_two))
    elif math_symbol == "//":
        print(number_one, math_symbol, number_two, "=", float(number_one) // float(number_two))
    else:
        print("Operator is not supported.")










