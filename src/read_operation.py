def get_operation():
    op = None
    while op not in ["1", "2", "3", "4", "5", "6", "7"]:
        op = str(input("please select desired operation\n\
        1 - median\n\
        2 - mode\n\
        3 - standard deviation\n\
        4 - coefficient of variation\n\
        5 - rising period (???)\n\
        6 - falling period (???)\n\
        7 - constant period (???)\n\
        8 - comparison (???)\n"))
        if op not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Invalid choice!")
        return op