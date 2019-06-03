def read_currency(a, b):
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
