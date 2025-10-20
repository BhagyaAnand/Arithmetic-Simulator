from gui.app import App

def detect_base(num_str):
    """Detect base of the number without prefixes"""
    num_str = num_str.upper()

    if all(ch in "01" for ch in num_str):
        return 2  # Binary
    elif all(ch in "01234567" for ch in num_str):
        return 8  # Octal
    elif all(ch in "0123456789" for ch in num_str):
        return 10  # Decimal
    elif all(ch in "0123456789ABCDEF" for ch in num_str):
        return 16  # Hexadecimal
    else:
        raise ValueError("Invalid number format!")

def to_decimal(num_str):
    """Convert detected number to decimal"""
    base = detect_base(num_str)
    return int(num_str, base), base

def from_decimal(num):
    """Convert decimal number to all number systems"""
    return {
        "Decimal": str(num),
        "Binary": bin(num)[2:],
        "Octal": oct(num)[2:],
        "Hexadecimal": hex(num)[2:].upper()
    }

def main():
    print("===== Arithmetic Operations Simulator =====")
    print("Enter numbers (Binary, Octal, Decimal, or Hex) without prefixes.")

    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    try:
        n1, base1 = to_decimal(num1)
        n2, base2 = to_decimal(num2)
    except ValueError as e:
        print(e)
        return

    print(f"Detected Base -> First number: {base1}, Second number: {base2}")
    print(f"Decimal Values -> {n1}, {n2}")

    print("Operations: +  -  *  /")
    op = input("Select operation: ")

    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        if n2 == 0:
            print("Error: Division by zero!")
            return
        result = n1 // n2
    else:
        print("Invalid operation!")
        return

    print("\n===== Result =====")
    for system, value in from_decimal(result).items():
        print(f"{system}: {value}")

if __name__ == "__main__":
    app = App()
    app.mainloop()