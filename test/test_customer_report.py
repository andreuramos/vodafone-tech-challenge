from unittest import TestCase

from src.customer import Customer
from src.customer_report import CustomerReport


class TestCustomerReport(TestCase):
    def test_empty_report(self):
        retport = CustomerReport()

        assert retport.avg_billing == 0

    def test_one_customer(self):
        report = CustomerReport()
        customer = Customer(1, "Name", "email", 1, "NY")

        report.add_customer(customer)

        assert report.avg_billing == 1

    def test_two_customers(self):
        report = CustomerReport()
        customer1 = Customer(1, "Name", "email@email", 5, "NJ")
        customer2 = Customer(2, "LongName", "email@domain", 10, "CA")

        report.add_customer(customer1)
        report.add_customer(customer2)

        assert report.avg_billing == 7.5