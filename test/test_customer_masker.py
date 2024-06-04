from unittest import TestCase

from src.customer import Customer
from src.customer_masker import CustomerMasker


class TestCustomerMasker(TestCase):
    def setUp(self) -> None:
        self.masker = CustomerMasker()

    def test_alfanumeric_name_is_transformed_to_x(self):
        customer = Customer(1, "John Hammond", "", 0, "")

        masked_customer = self.masker.mask(customer)

        assert masked_customer.name == "XXXX XXXXXXX"

    def test_email_keeps_at_and_dot(self):
        customer = Customer(1, "", "johntravolta@mail.com", 0, "")

        masked_customer = self.masker.mask(customer)

        assert masked_customer.email == "XXXXXXXXXXXX@XXXX.XXX"

    def test_acute_characters_are_also_transformed_to_x(self):
        customer = Customer(1, "Jöhn Cénâ", "", 0, "")

        masked_customer = self.masker.mask(customer)

        assert masked_customer.name == "XXXX XXXX"