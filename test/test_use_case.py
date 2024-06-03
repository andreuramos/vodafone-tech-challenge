import unittest
from unittest.mock import MagicMock

from src.use_case import UseCase


class TestUseCase(unittest.TestCase):
    def test_fetches_customer_data(self):
        reader = MagicMock()
        use_case = UseCase(reader)

        use_case.run()

        reader.read.assert_called()


if __name__ == '__main__':
    unittest.main()
