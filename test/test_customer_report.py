from unittest import TestCase

from src.customer import Customer
from src.customer_report import CustomerReport


class TestCustomerReport(TestCase):
    def test_empty_report(self):
        report = CustomerReport()

        assert report.name_max_length == 0
        assert report.name_min_length is None
        assert report.name_avg_length == 0
        assert report.max_billing == 0
        assert report.min_billing is None
        assert report.avg_billing == 0

    def test_one_customer(self):
        report = CustomerReport()
        customer = Customer(1, "John", "email", 1, "NY")

        report.add_customer(customer)

        assert report.name_max_length == 4
        assert report.name_min_length == 4
        assert report.name_avg_length == 4
        assert report.max_billing == 1
        assert report.min_billing == 1
        assert report.avg_billing == 1

    def test_two_customers(self):
        report = CustomerReport()
        customer1 = Customer(1, "John", "email@email", 5, "NJ")
        customer2 = Customer(2, "LongJohn", "email@domain", 10, "CA")

        report.add_customer(customer1)
        report.add_customer(customer2)

        assert report.name_max_length == 8
        assert report.name_min_length == 4
        assert report.name_avg_length == 6
        assert report.max_billing == 10
        assert report.min_billing == 5
        assert report.avg_billing == 7.5

    def test_prints_as_expected(self):
        report = CustomerReport()
        customer1 = Customer(1, "John", "email@email", 500, "NJ")
        customer2 = Customer(2, "LongJohn", "email@domain", 2000, "CA")

        report.add_customer(customer1)
        report.add_customer(customer2)

        self.assertEqual(str(report),
                         "Name: Max. 8, Min. 4, Avg. 6.0\nBilling: Max. 2000.00, Min. 500.00, Avg. 1250.00")
