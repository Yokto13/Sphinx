from abc import ABC, abstractmethod


class AbstractStatistcs(ABC):
    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def dump(self):
        pass

    @abstractmethod
    def load(self):
        pass

    @abstractmethod
    def update(self):
        pass
