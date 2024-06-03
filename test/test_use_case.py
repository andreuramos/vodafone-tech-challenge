import unittest
from unittest.mock import MagicMock

from src.use_case import UseCase


class TestUseCase(unittest.TestCase):
    def test_fetches_customer_data(self):
        repository = MagicMock()
        use_case = UseCase(repository)

        use_case.run()

        repository.get.assert_called()


if __name__ == '__main__':
    unittest.main()
