def read_margin():
    mrg = str(input("please specify the accuracy of rates\n\
        1 - 1 place after coma\n\
        2 - 2 places after coma\n\
        3 - 3 places after coma\n\
        4 - 4 places after coma"))
    if mrg not in ["1", "2", "3", "4"]:
        print("invalid input")
        return None
    else:
        return mrg
