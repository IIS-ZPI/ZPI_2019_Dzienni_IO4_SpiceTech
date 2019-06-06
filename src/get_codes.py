import requests


def get_codes():
    """
    Requests tables containing current rates for all currencies from the NBP server.
    If the request came across OK (code 200), all 3-letter currency codes are extracted from
    the two tables (A and B) and parsed into two separate arrays.
    Intended to be used to obtain a list of all currencies available to be chosen by the user in the program.

    Arguments: none

    Returns: two arrays of strings if the request came across OK, or two None objects otherwise
    """
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
