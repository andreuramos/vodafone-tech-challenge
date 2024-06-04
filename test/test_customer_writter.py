from unittest import TestCase

from src.customer import Customer
from src.customer_writer import CustomerWriter
import os.path


class TestCustomerWriter(TestCase):

    def setUp(self) -> None:
        self.writer = CustomerWriter()

    def test_creates_file_if_not_exists(self):
        writer = CustomerWriter("data/test_output.csv")

        writer.write([], 0)

        assert os.path.isfile("data/test_output.csv")

    def test_file_contains_expected_output(self):
        customer = Customer(1,"John Goodman", "jgoodman@email.com", 0, "NY")
        writer = CustomerWriter("data/test_output.csv")

        writer.write([customer], 0)

        file = open("data/test_output.csv", "r")
        header = file.readline()
        data = file.readline()
        file.close()
        assert header == "ID,Name,Email,Billing,Location\n"
        assert data == "1,John Goodman,jgoodman@email.com,0,NY\n"

    def tearDown(self) -> None:
        try:
            os.remove("data/test_output.csv")
        except OSError:
            pass
