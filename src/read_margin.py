def read_margin():
    """
    Takes user input to decide how many places after decimal point to round the array
    :return: number of places after decimal point
    """
    mrg = str(input("please specify the accuracy of rates\n\
        1 - 1 place after decimal point\n\
        2 - 2 places after decimal point\n\
        3 - 3 places after decimal point\n\
        4 - 4 places after decimal point"))
    if mrg not in ["1", "2", "3", "4"]:
        print("invalid input")
        return None
    else:
        return mrg
