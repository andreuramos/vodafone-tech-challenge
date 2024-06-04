from src.customer import Customer


class CustomerReport:
    def __init__(self):
        self.number_of_customers = 0
        self.avg_billing = 0

    def add_customer(self, customer: Customer):
        self.number_of_customers += 1
        self.avg_billing += (customer.billing - self.avg_billing) / self.number_of_customers