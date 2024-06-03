from abc import ABC, abstractmethod


class CustomerRepository(ABC):

    @abstractmethod
    def get(self) -> list:
        pass
