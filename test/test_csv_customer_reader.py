from unittest import TestCase

from src.csv_customer_reader import CsvCustomerReader


class TestCsvCustomerReader(TestCase):

    def test_no_source_file_throws_exception(self):
        reader = CsvCustomerReader('test/nofile.csv')

        with self.assertRaises(FileNotFoundError):
            reader.read()


    def test_empty_file_throws_exception(self) -> None:
        reader = CsvCustomerReader('test/empty.csv')

        with self.assertRaises(ValueError) as context:
            reader.read()

        self.assertEqual(str(context.exception), "Source file is empty")

    def test_valid_file_returns_customer_list(self):
        reader = CsvCustomerReader('test/example.csv')

        customers = reader.read()

        assert len(customers) == 5
        assert customers[0].id == 1
        assert customers[0].name == "John Smith"
        assert customers[0].email == "john@mail.com"
        assert customers[0].billing == 15000
        assert customers[0].location == "New York"
        assert customers[2].billing == 0
        assert customers[3].billing == 12400.27


