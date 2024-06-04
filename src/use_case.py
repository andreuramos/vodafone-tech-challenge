from src.customer_masker import CustomerMasker
from src.customer_reader import CustomerReader
from src.customer_report import CustomerReport
from src.customer_writer import CustomerWriter


class UseCase:
    def __init__(self,
                 customer_reader: CustomerReader,
                 customer_masker: CustomerMasker,
                 customer_writer: CustomerWriter):
        self.customerRepository = customer_reader
        self.customer_masker = customer_masker
        self.customer_writer = customer_writer

    def run(self) -> list:
        masked_customers = []
        report = CustomerReport()
        try:
            for customer in self.customerRepository.read():
                report.add_customer(customer)
                masked_customers.append(self.customer_masker.mask(customer))
        except FileNotFoundError:
            return [0, "File not found"]
        except Exception as e:
            return [0, f"Error: {e}"]

        self.customer_writer.write(masked_customers, report.avg_billing)

        return [1, "OK"]

