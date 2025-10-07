def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        denom = float(denominator)
        result = num / denom
        print(f"The result of the division is {result}")
        return
    except ValueError:
        print("Error: Please enter numeric values only.")
        return
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return