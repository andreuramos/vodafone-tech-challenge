from src.csv_customer_reader import CsvCustomerReader
from src.customer_masker import CustomerMasker
from src.customer_writer import CustomerWriter
from src.use_case import UseCase

if __name__ == '__main__':
    reader = CsvCustomerReader()
    masker = CustomerMasker()
    writer = CustomerWriter()
    use_case = UseCase(reader, masker, writer)

    [code, message] = use_case.run()

    print(message)