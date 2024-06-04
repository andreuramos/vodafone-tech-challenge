from src.customer import Customer


class CustomerReport:
    def __init__(self):
        self.number_of_customers = 0
        self.name_max_length = None
        self.name_min_length = None
        self.name_avg_length = None
        self.avg_billing = 0

    def add_customer(self, customer: Customer):
        self.number_of_customers += 1

        if self.name_max_length is None:
            self.name_max_length = len(customer.name)
        else:
            self.name_max_length = max(self.name_max_length, len(customer.name))

        if self.name_min_length is None:
            self.name_min_length = len(customer.name)
        else:
            self.name_min_length = min(self.name_min_length, len(customer.name))

        if self.name_avg_length is None:
            self.name_avg_length = 0
        self.name_avg_length += (len(customer.name) - self.name_avg_length) / self.number_of_customers

        self.avg_billing += (customer.billing - self.avg_billing) / self.number_of_customers
