from unittest import TestCase

from src.csv_customer_reader import CsvCustomerReader


class TestCsvCustomerReader(TestCase):
    def test_empty_file_throws_exception(self) -> None:
        reader = CsvCustomerReader()

        reader.read()

    # def test_not_found_column_throws_exception
    # def test_correct_file_returns_customer_list