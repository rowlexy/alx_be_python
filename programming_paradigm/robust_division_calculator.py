def safe_divide(numerator, denominator):
        numerator = float(input("Enter a number: "))
        denominator = float(input("Enter a number: "))
        result = numerator / denominator
        print(f"The result of the division is {result:.1f}")
try:
    safe_divide(10, 2)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Please enter numeric values only.")

