import re

from src.customer import Customer


def _mask_string(name: str) -> str:
    return re.sub('[\w]', 'X', name)


class CustomerMasker:
    def mask(self, customer: Customer) -> Customer:
        customer.name = _mask_string(customer.name)
        customer.email = _mask_string(customer.email)
        return customer
