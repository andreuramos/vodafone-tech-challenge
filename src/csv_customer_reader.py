from src.customer import Customer
from src.customer_reader import CustomerReader
import os


def _parse_billing(billing) -> float:
    try:
        billing = float(billing)
    except ValueError:
        billing = 0.0
    return billing


def _build_customer(line):
    [id, name, email, billing, location] = line.split(',')
    customer = Customer(
        int(id),
        name.strip(),
        email.strip(),
        _parse_billing(billing),
        location.strip()
    )
    return customer


class CsvCustomerReader(CustomerReader):

    def __init__(self, source_path=None):
        if source_path is None:
            data_directory = os.getenv('DATA_DIRECTORY')
            source_file = os.getenv('INPUT_FILE')
            self.file_path = data_directory + '/' + source_file
        else:
            self.file_path = source_path

    def read(self) -> list:
        customers = []

        file = open(self.file_path, "r")
        file.readline()

        data_lines = file.readlines()
        if len(data_lines) == 0:
            file.close()
            raise ValueError('Source file is empty')
        file.close()

        for line in data_lines:
            customer = _build_customer(line)
            customers.append(customer)

        return customers
