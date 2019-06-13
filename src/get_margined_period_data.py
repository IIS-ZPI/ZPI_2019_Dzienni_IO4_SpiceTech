import numpy


def get_margined_period_data(period_data, margin):
    """
    Rounds the period data table to X places after the coma, specified by margin
    :param period_data: array of floats
    :param margin: unsigned int
    :return: array of floats
    """
    return numpy.around(period_data, margin)
