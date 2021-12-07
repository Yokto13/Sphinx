from dataclasses import dataclass
from abstract_statistics import AbstractStatistcs


@dataclass
class ScoreStastics(AbstractStatistcs):
    total: int = 0
    correct: int = 0

    def __str__(self):
        return f"{self.correct} correct from {self.total} total."

    def update(self, correctly_answered: bool):
        self.correct += 1 if correctly_answered else 0
        self.total += 1

    def dump(self):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError

    def __eq__(self, other):
        return type(self) == type(other) and self.total == other.total and self.correct == other.correct




