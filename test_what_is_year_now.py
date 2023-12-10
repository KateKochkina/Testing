import unittest
from unittest.mock import patch
from year_now import what_is_year_now


class TestWhatIsYearNow(unittest.TestCase):
    def set_return_value(self, mocked_urlopen, value: str):
        mocked_context_manager = mocked_urlopen.return_value.__enter__.return_value
        mocked_context_manager.read.return_value = value

    @patch('year_now.urllib.request.urlopen')
    def test_year_in_YYYY_MM_DD_format(self, mocked_urlopen):
        self.set_return_value(
            mocked_urlopen, '{"currentDateTime": "2023-11-01"}'
        )
        self.assertEqual(what_is_year_now(), 2023)

    @patch('year_now.urllib.request.urlopen')
    def test_year_in_DD_MM_YYYY_format(self, mocked_urlopen):
        self.set_return_value(
            mocked_urlopen, '{"currentDateTime": "01.11.2023"}'
        )
        self.assertEqual(what_is_year_now(), 2023)

    @patch('year_now.urllib.request.urlopen')
    def test_invalid_date_format(self, mocked_urlopen):
        self.set_return_value(
            mocked_urlopen, '{"currentDateTime": "2023/11/01"}'
        )
        with self.assertRaises(ValueError):
            what_is_year_now()


if __name__ == '__main__':
    unittest.main()
