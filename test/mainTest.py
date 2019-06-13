import unittest
import sys
from dateutil.relativedelta import relativedelta
import datetime
sys.path.append("./src/")

import read_period
import get_period_data
import get_codes
import read_currency
import read_operation
import get_number_of_sessions

class MainTest(unittest.TestCase):

    def test_read_period(self):
        read_period.input = lambda _: "10"
        self.assertEqual(read_period.read_period(), None)
        read_period.input = lambda _: "1"

    def test_get_period_data(self):
        period = datetime.datetime.now().date()
        table_code = "A"
        currency_code = "USD"
        self.assertGreater(len(get_period_data.get_period_data(period, table_code, currency_code)), 0)

        table_code = "B"
        self.assertEqual(len(get_period_data.get_period_data(period, table_code, currency_code)), 0)

    def test_get_codes(self):
        res = (['THB', 'USD', 'AUD', 'HKD', 'CAD', 'NZD', 'SGD', 'EUR', 'HUF', 'CHF', 'GBP', 'UAH', 'JPY', 'CZK', 'DKK', 'ISK', 'NOK', 'SEK', 'HRK', 'RON', 'BGN', 'TRY', 'ILS', 'CLP', 'PHP', 'MXN', 'ZAR', 'BRL', 'MYR', 'RUB', 'IDR', 'INR', 'KRW', 'CNY', 'XDR'], ['AFN', 'MGA', 'PAB', 'ETB', 'VES', 'BOB', 'CRC', 'SVC', 'NIO', 'GMD', 'MKD', 'DZD', 'BHD', 'IQD', 'JOD', 'KWD', 'LYD', 'RSD', 'TND', 'MAD', 'AED', 'STN', 'BSD', 'BBD', 'BZD', 'BND', 'FJD', 'GYD', 'JMD', 'LRD', 'NAD', 'SRD', 'TTD', 'XCD', 'SBD', 'VND', 'AMD', 'CVE', 'AWG', 'BIF', 'XOF', 'XAF', 'XPF', 'DJF', 'GNF', 'KMF', 'CDF', 'RWF', 'EGP', 'GIP', 'LBP', 'SSP', 'SDG', 'SYP', 'GHS', 'HTG', 'PYG', 'ANG', 'PGK', 'LAK', 'MWK', 'ZMW', 'AOA', 'MMK', 'GEL', 'MDL', 'ALL', 'HNL', 'SLL', 'SZL', 'LSL', 'AZN', 'MZN', 'NGN', 'ERN', 'TWD', 'TMT', 'MRU', 'TOP', 'MOP', 'ARS', 'DOP', 'COP', 'CUP', 'UYU', 'BWP', 'GTQ', 'IRR', 'YER', 'QAR', 'OMR', 'SAR', 'KHR', 'BYN', 'LKR', 'MVR', 'MUR', 'NPR', 'PKR', 'SCR', 'PEN', 'KGS', 'TJS', 'UZS', 'KES', 'SOS', 'TZS', 'UGX', 'BDT', 'WST', 'KZT', 'MNT', 'VUV', 'BAM'])
        self.assertEqual(get_codes.get_codes(), res)

    def test_read_currency(self):
        a = ["USD", "GBP"]
        b = ["PL", "NIS"]

        for i in a:
            read_currency.input = lambda _: i
            self.assertEqual(read_currency.read_currency(a, b), (i, "A"))

        for i in b:
            read_currency.input = lambda _: i
            self.assertEqual(read_currency.read_currency(a, b), (i, "B"))

    def test_read_operation(self):
        inp = [str(x) for x in range(0, 10)]
        res = [None, "1", "2", "3", None, None, None, None, None, None]
        for i,r in zip(inp, res):
            read_operation.input = lambda _: i
            self.assertEqual(read_operation.read_operation(), r)

    def test_read_period(self):
        read_period.input = lambda _: 1
        rel = relativedelta(days=7)
        self.assertEqual(read_period.read_period(), datetime.datetime.now().date() - rel)

    def test_get_number_of_sessions(self):
        inp = [0, 0.1, 0.2, 0.3, 0.1, 0.4, 0.7, 1, 0]
        res = (2,2,0)
        self.assertEqual(get_number_of_sessions.get_number_of_sessions(inp), res)

        inp = [0,0,0,1,2,3,0,0,0]
        res = (1,1,2)
        self.assertEqual(get_number_of_sessions.get_number_of_sessions(inp), res)

if __name__ == '__main__':
    unittest.main()
