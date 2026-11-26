"""A small command-line calculator for the UCS 745 Git lab."""

def calculate(first, second, operator):
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("You cannot divide by zero.")
        return first / second
    raise ValueError("Use one of these operators: +, -, *, /")


def main():
    print("Simple Calculator")
    try:
        first = float(input("Enter the first number: "))
        operator = input("Enter an operator (+, -, *, /): ").strip()
        second = float(input("Enter the second number: "))
        answer = calculate(first, second, operator)
        print("Answer:", answer)
    except (ValueError, ZeroDivisionError) as error:
        print("Error:", error)


if __name__ == "__main__":
    main()
