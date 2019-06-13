from datetime import datetime
import numpy
from scipy import stats
import get_codes
import read_currency
import read_operation
import read_period
import get_period_data
import read_margin
import get_margined_period_data
import get_number_of_sessions

A, B = get_codes.get_codes()

data = None
response = None
values = []
operation = None
currency_code = None
table_code = None
period = None
while operation is None:
    operation = read_operation.read_operation()
if operation in ["1", "2"]:
    while currency_code is None:
        currency_code, table_code = read_currency.read_currency(A, B)
    while period is None:
        period = read_period.read_period()
    values = get_period_data.get_period_data(period, table_code, currency_code)
    if operation == "1":
        print("start: {0}, end: {1}, currency: {2}".format(period, datetime.today().date(), currency_code))
        print("Median: \t\t\t\t\t{0}".format(numpy.median(values)))
        answer, count = stats.mode(values)
        print("Mode: \t\t\t\t\t\t{0}".format(answer[0]))
        print("Standard deviation: \t\t{0}".format(numpy.std(values)))
        print("Coefficient of variation: \t{0}".format(stats.variation(values)))
    if operation == "2":
        margin = None
        while margin is None:
            margin = read_margin.read_margin()
        values = get_margined_period_data.get_margined_period_data(values, margin)
        rise, fall, stay = get_number_of_sessions.get_number_of_sessions(values)
        print("start: {0}, end: {1}, currency: {2}".format(period, datetime.today().date(), currency_code))
        print("rising sessions: \t{0}".format(rise))
        print("falling sessions: \t{0}".format(fall))
        print("constant sessions: \t{0}".format(stay))

elif operation == "3":
    currency_code1 = None
    currency_code2 = None
    print("Input two codes of the currencies you want to compare")
    while currency_code1 is None:
        currency_code1, table_code1 = read_currency.read_currency(A, B)
    while currency_code2 is None:
        currency_code2, table_code2 = read_currency.read_currency(A, B)
    starting_date = str(input("Input starting date in YYYY-MM-DD format"))
    ending_date = str(input("Input ending date in YYYY-MM-DD format"))
    print("This feature is not implemented yet!")
