def get_currency_pair_analysis(period_data1, period_data2):
    if len(period_data1) != len(period_data2):
        print("massive error, nbp error yo")
        return None

    comb_data = []
    for data in range(1, len(period_data1):
        comb_data.append((period_data1[data]*period_data2[data-1])/(period_data1[data-1]*period_data2[data]))

    return comb_data