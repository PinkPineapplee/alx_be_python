def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        print(f"The result of the division is {result}\n")

    except ValueError:
        print("Error: Please enter numeric values only.\n")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.\n")