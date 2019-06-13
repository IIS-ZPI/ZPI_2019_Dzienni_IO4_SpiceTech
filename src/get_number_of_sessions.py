
def get_number_of_sessions(period_data):
    """
    Function iterates through an array and checks if the next value is greater or smaller than the previous
    :param period_data: array of floats
    :return: three integers corresponding to rising session, falling session, and no change
    """
    rise=0
    fall=0
    stay=0
    for data in range(1, len(period_data)):
        if period_data[data] > period_data[data-1]:
            rise += 1
        elif period_data[data] < period_data[data-1]:
            fall += 1
        else:
            stay += 1
    return rise, fall, stay
