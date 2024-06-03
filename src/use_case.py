from src.customer_repository import CustomerRepository


class UseCase:
    def __init__(self, customer_repository: CustomerRepository):
        self.customerRepository = customer_repository

    def run(self):
        self.customerRepository.get()
