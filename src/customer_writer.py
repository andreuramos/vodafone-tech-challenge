import os

from src.customer import Customer


class CustomerWriter:

    def __init__(self, outputpath=None):
        if outputpath is None:
            data_directory = os.getenv('DATA_DIRECTORY')
            if not os.path.exists(data_directory):
                os.makedirs(data_directory)
            output_filename = os.getenv('OUTPUT_FILE')
            self.outputpath = data_directory + '/' + output_filename
        else:
            self.outputpath = outputpath

    def write(self, customers: list, average_billing: float) -> None:
        self.__remove_existing_file()

        with open(self.outputpath, "w") as file:
            file.write("ID,Name,Email,Billing,Location\n")
            for customer in customers:
                file.write(self.__build_csv_line(customer, average_billing) + "\n")

        file.close()

    def __remove_existing_file(self):
        try:
            os.remove(self.outputpath)
        except OSError:
            pass

    @staticmethod
    def __build_csv_line(customer: Customer, average_billing: float):
        return ','. join([
            str(customer.id),
            customer.name,
            customer.email,
            str(average_billing),
            customer.location
        ])