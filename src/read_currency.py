def read_currency(a, b):
    """
    Reads input from the user and checks if such a currency code exists in the table A, B, or neither of them.

    Arguments: two arrays of strings

    Returns: two strings (currency code and the table it belongs to) if the input was correct, or
    two None objects otherwise
    """
    cc = None
    tc = None
    inp = str(input("input 3-letter currency code (eg. USD)\n")).upper()
    if inp in a:
        cc = inp
        tc = "A"
    elif inp in b:
        cc = inp
        tc = "B"
    else:
        print("Invalid code!")
    return cc, tc
