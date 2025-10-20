def detect_base(num_str: str) -> int:
    """
    Detect the number system based on characters.
    Rules:
      - Only 0 and 1 => Binary
      - Only digits 0–7 => Octal
      - Only digits 0–9 => Decimal
      - Contains A–F => Hexadecimal
    """
    num_str = num_str.upper()

    if all(ch in "01" for ch in num_str):
        return 2
    elif all(ch in "01234567" for ch in num_str):
        return 8
    elif all(ch in "0123456789" for ch in num_str):
        return 10
    elif all(ch in "0123456789ABCDEF" for ch in num_str):
        return 16
    else:
        raise ValueError(f"Invalid number format: {num_str}")

def to_decimal(num_str: str) -> tuple[int, int]:
    """Convert detected number to decimal and return (value, base)."""
    base = detect_base(num_str)
    return int(num_str, base), base

def from_decimal(num: int) -> dict:
    """Convert decimal number to all number systems."""
    return {
        "Decimal": str(num),
        "Binary": bin(num)[2:],
        "Octal": oct(num)[2:],
        "Hexadecimal": hex(num)[2:].upper()
    }