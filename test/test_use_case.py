import unittest
from unittest.mock import MagicMock

from src.use_case import UseCase
from src.customer import Customer


class TestUseCase(unittest.TestCase):

    def setUp(self) -> None:
        self.reader = MagicMock()
        self.masker = MagicMock()
        self.writer = MagicMock()

    def test_file_not_found_returns_error(self):
        self.reader.read.side_effect = FileNotFoundError()
        use_case = UseCase(self.reader, self.masker, self.writer)

        [code, message] = use_case.run()

        assert code == 0
        assert message == "File not found"

    def test_no_customers(self):
        use_case = UseCase(self.reader, self.masker, self.writer)

        [code, message] = use_case.run()

        self.masker.assert_not_called()
        assert code == 1
        assert message == "OK"

    def test_one_customer(self):
        customer = Customer()
        masked_customer = Customer()
        self.reader.read.return_value = [customer]
        self.masker.mask.return_value = masked_customer
        use_case = UseCase(self.reader, self.masker, self.writer)

        [code, message] = use_case.run()

        self.reader.read.assert_called()
        self.masker.mask.assert_called_with(customer)
        self.writer.write.assert_called_with([masked_customer])
        assert code == 1
        assert message == "OK"


if __name__ == '__main__':
    unittest.main()
