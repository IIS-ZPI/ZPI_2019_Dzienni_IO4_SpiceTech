import requests
import numpy
from scipy import stats
import get_codes
import read_currency
import read_operation

A, B = get_codes.get_codes()

data = None
response = None
values = []
operation = None
currency_code = None
table_code = None
while operation is None:
    operation = read_operation.read_operation()
if operation in ["1", "2", "3", "4", "5"]:
    while currency_code is None:
        currency_code, table_code = read_currency.read_currency(A, B)
    starting_date = str(input("Input starting date in YYYY-MM-DD format"))
    ending_date = str(input("Input ending date in YYYY-MM-DD format"))
    url = str("http://api.nbp.pl/api/exchangerates/rates/{0}/{1}/{2}/{3}/?format=json".format(\
                                                    table_code, currency_code, starting_date, ending_date))
    response = requests.get(url)
    if response.status_code != 200:
        print("Error: request returned code: " + str(response.status_code))
    else:
        data = response.json()
        for x in data["rates"]:
            values.append(x["mid"])
        if operation == "1":
            answer = numpy.median(values)
            print("The median for " + currency_code + " in the period from " + starting_date + " to " + ending_date + " is: " + str(answer))
        if operation == "2":
            answer, count = stats.mode(values)
            print("The mode for " + currency_code + " in the period from " + starting_date + " to " + ending_date + " is: " + str(answer[0]))
            print("TEST: count == " + str(count))
        if operation == "3":
            answer = numpy.std(values)
            print("The standard deviation for " + currency_code + " in the period from " + starting_date + " to " + ending_date + " is: " + str(answer))
        if operation == "4":
            answer = stats.variation(values)
            print("The coefficient of variation for " + currency_code + " in the period from " + starting_date + " to " + ending_date + " is: " + str(answer))
        if operation == "5":
            print("This feature is not implemented yet!")
elif operation == "6":
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