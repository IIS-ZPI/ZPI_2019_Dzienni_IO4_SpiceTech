def read_operation():
    """
    Presents a list of available options to the user, and takes input from console
    Is intended to be called inside a loop until correct input is provided

    Arguments: none

    Returns: string if input is on the list of allowed choices, or None otherwise
    """

    op = str(input("please select desired operation\n\
    1 - median\n\
    2 - mode\n\
    3 - standard deviation\n\
    4 - coefficient of variation\n\
    5 - periods of change\n\
    6 - comparison\n"))
    if op not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid choice!")
        op = None
    return op
