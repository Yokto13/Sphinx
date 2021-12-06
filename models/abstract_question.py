from abc import ABC, abstractmethod


class AbstractQuestion(ABC):
    @abstractmethod
    def __init__(self):
        self._question = None
        self._answer = None

    @property
    @abstractmethod
    def question(self):
        pass

    @question.setter
    @abstractmethod
    def question(self, val):
        self._question = val

    @property
    @abstractmethod
    def answer(self):
        pass

    @question.setter
    @abstractmethod
    def answer(self, val):
        self._answer = val
