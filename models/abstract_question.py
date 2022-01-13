from abc import ABC, abstractmethod


class AbstractQuestion(ABC):
    @abstractmethod
    def __init__(self, *args):
        pass

    @property
    @abstractmethod
    def question(self):
        pass

    @question.setter
    @abstractmethod
    def question(self, val):
        pass

    @property
    @abstractmethod
    def answer(self):
        pass

    @question.setter
    @abstractmethod
    def answer(self, val):
        pass

    def __str__(self):
        pass

    @property
    @abstractmethod
    def score(self):
        pass
