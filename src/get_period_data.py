from datetime import datetime
from dateutil.relativedelta import relativedelta
import math
import requests


def get_period_data(period, table_code, currency_code):
    period_data = []
    today = datetime.today().date()
    iterations = math.ceil((today - period).days/93)
    for i in range(0, iterations):
        if i != iterations-1:
            temp_period = period + relativedelta(days=93)
            print("start: {0}, end: {1}, num_of_days: {2}".format(period, temp_period, temp_period - period))
            url = str("http://api.nbp.pl/api/exchangerates/rates/{0}/{1}/{2}/{3}/?format=json".format(
                table_code, currency_code, period, temp_period))
            response = requests.get(url)
            if response.status_code != 200:
                print("Error: request returned code: " + str(response.status_code))
            else:
                data = response.json()
                for x in data["rates"]:
                    period_data.append(x["mid"])
                period = temp_period + relativedelta(days=1)
        else:
            print("start: {0}, end: {1}, num_of_days: {2}".format(period, today, today - period))
            url = str("http://api.nbp.pl/api/exchangerates/rates/{0}/{1}/{2}/{3}/?format=json".format(
                table_code, currency_code, period, today))
            response = requests.get(url)
            if response.status_code != 200:
                print("Error: request returned code: " + str(response.status_code))
            else:
                data = response.json()
                for x in data["rates"]:
                    period_data.append(x["mid"])
    return period_data
