from src.customer import Customer


class CustomerReport:
    def __init__(self):
        self.number_of_customers = 0
        self.name_max_length = 0
        self.name_min_length = None
        self.name_avg_length = 0
        self.max_billing = 0
        self.min_billing = None
        self.avg_billing = 0

    def add_customer(self, customer: Customer):
        self.number_of_customers += 1

        self.name_max_length = max(self.name_max_length, len(customer.name))

        if self.name_min_length is None:
            self.name_min_length = len(customer.name)
        else:
            self.name_min_length = min(self.name_min_length, len(customer.name))

        self.name_avg_length += (len(customer.name) - self.name_avg_length) / self.number_of_customers

        self.max_billing = max(self.max_billing, customer.billing)

        if self.min_billing is None:
            self.min_billing = customer.billing
        else:
            self.min_billing = min(self.min_billing, customer.billing)

        self.avg_billing += (customer.billing - self.avg_billing) / self.number_of_customers

    def __str__(self):
        name_stats = f'Name: Max. {self.name_max_length}, Min. {self.name_min_length}, Avg. {self.name_avg_length}'
        billing_stats = f'Billing: Max. {self.max_billing:.2f}, Min. {self.min_billing:.2f}, Avg. {self.avg_billing:.2f}'

        return f'{name_stats}\n{billing_stats}'
