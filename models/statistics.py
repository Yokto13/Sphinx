from dataclasses import dataclass
from .abstract_statistics import AbstractStatistcs


@dataclass
class ScoreStatistics(AbstractStatistcs):
    def __init__(self, raw=None):
        if raw is None:
            self.correct: int = 0
            self.total: int = 0
        else:
            self.correct, self.total = map(int, raw.split(','))

    def __str__(self):
        return f"{self.correct} correct from {self.total} total."

    def update(self, correctly_answered: bool):
        self.correct += 1 if correctly_answered else 0
        self.total += 1

    def dump(self):
        return f"{self.correct},{self.total}"

    def __eq__(self, other):
        return type(self) == type(other) and self.total == other.total and self.correct == other.correct




