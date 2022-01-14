from abc import ABC, abstractmethod


class AbstractStatistcs(ABC):
    @abstractmethod
    def __init__(self, *args):
        # Args can be used for building from dumped strings.
        # Init needs to implement load from string.
        pass

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def dump(self):
        pass

    @abstractmethod
    def update(self, *args):
        pass
