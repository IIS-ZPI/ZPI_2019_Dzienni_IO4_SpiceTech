from datetime import datetime
from dateutil.relativedelta import relativedelta


def read_period():
    period = 0
    prd = str(input("please select desired period\n\
    1 - 1 week\n\
    2 - 2 weeks\n\
    3 - 1 month\n\
    4 - 2 months\n\
    5 - quarter of the year\n\
    6 - half of the year\n\
    7 - whole year\n"))
    if prd not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("invalid input")
        return None
    elif prd == "1":
        period = relativedelta(days=7)
    elif prd == "2":
        period = relativedelta(days=14)
    elif prd == "3":
        period = relativedelta(months=1)
    elif prd == "4":
        period = relativedelta(months=2)
    elif prd == "5":
        period = relativedelta(months=3)
    elif prd == "6":
        period = relativedelta(months=6)
    elif prd == "7":
        period = relativedelta(years=1)
    return (datetime.today() - period).date()
