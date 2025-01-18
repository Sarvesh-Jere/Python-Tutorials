result = 0
operator = ""
number_1 = 0

while True:
    if len(operator) == 0:
        number_1 = int(input("Enter the First number: "))
        result = number_1

    operator = input("Enter the operator from (-, +, *, /) and = to get the result: ")

    if operator == "=":
        print("Result is", result)
        break

    number_2 = int(input("Enter your second number: "))

    if operator == "+":
        result += number_2
    elif operator == "-":
        result -= number_2
    elif operator == "*":
        result *= number_2
    elif operator == "/":
        if number_2 == 0:
            print("Cannot divide by 0")
            break
        else:
            result /= number_2
    else:
        print("Invalid operator. Please try again.")
        continue  # Restart loop for invalid operator

    print("Intermediate result:", result)

    # Reset operator for the next iteration
    operator = ""


