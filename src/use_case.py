from src.customer_masker import CustomerMasker
from src.customer_reader import CustomerReader


class UseCase:
    def __init__(self, customer_reader: CustomerReader, customer_masker: CustomerMasker):
        self.customerRepository = customer_reader
        self.customer_masker = customer_masker

    def run(self):
        masked_customers = []
        for customer in self.customerRepository.read():
            masked_customers.append(self.customer_masker.mask(customer))
