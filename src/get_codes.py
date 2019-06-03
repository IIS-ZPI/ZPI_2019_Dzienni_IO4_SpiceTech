import requests


def get_codes():
    a = []
    b = []
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/A/?format=json")
    info = response.json()
    if response.status_code != 200:
        return None, None
    for x in info[0]["rates"]:
        a.append(x["code"])
    response = requests.get("http://api.nbp.pl/api/exchangerates/tables/B/?format=json")
    info = response.json()
    if response.status_code != 200:
        return None, None
    for x in info[0]["rates"]:
        b.append(x["code"])
    return a, b
