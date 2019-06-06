import unittest
import sys
import datetime
sys.path.append("./src/")

import get_period_data
import get_codes
import read_currency
import read_operation

class MainTest(unittest.TestCase):

    def test_get_period_data(self):
        period = datetime.datetime.now().date()
        table_code = "A"
        currency_code = "USD"
        self.assertGreater(len(get_period_data.get_period_data(period, table_code, currency_code)), 0)

        table_code = "B"
        self.assertEqual(len(get_period_data.get_period_data(period, table_code, currency_code)), 0)

    def test_read_operation(self):
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
        res = [None, "1", "2", "3", "4", "5", "6", None, None, None]
        for i,r in zip(inp, res):
            read_operation.input = lambda _: i
            self.assertEqual(read_operation.read_operation(), r)

if __name__ == '__main__':
    unittest.main()
