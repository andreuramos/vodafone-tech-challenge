from src.customer_reader import CustomerReader


class UseCase:
    def __init__(self, customer_reader: CustomerReader):
        self.customerRepository = customer_reader

    def run(self):
        self.customerRepository.read()
