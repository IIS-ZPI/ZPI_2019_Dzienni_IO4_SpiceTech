import requests


def get_codes():
    a = []
    b = []
    info = (requests.get("http://api.nbp.pl/api/exchangerates/tables/A/?format=json")).json()
    for x in info[0]["rates"]:
        a.append(x["code"])
    info = (requests.get("http://api.nbp.pl/api/exchangerates/tables/B/?format=json")).json()
    for x in info[0]["rates"]:
        b.append(x["code"])
    return a, b