import numpy


def get_margined_period_data(period_data, margin):
    return numpy.around(period_data, margin)
