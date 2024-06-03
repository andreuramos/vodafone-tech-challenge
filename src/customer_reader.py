from abc import ABC, abstractmethod


class CustomerReader(ABC):

    @abstractmethod
    def read(self) -> list:
        pass
