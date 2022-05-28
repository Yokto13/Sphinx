from .abstract_question import AbstractQuestion
from .statistics_holder import StatisticsHolder
from .statistics import ScoreStatistics


class BasicQuestion(AbstractQuestion):
    def __init__(self, question=None, answer=None):
        self._question: str = question
        self._answer: str = answer
        self._score = 0
        self._last_used = 0

    @property
    def question(self):
        return self._question

    @property
    def answer(self):
        return self._answer

    @question.setter
    def question(self, val: str):
        self._question = val

    @answer.setter
    def answer(self, val: str):
        self._answer = val

    def __str__(self):
        return f"{self.question},{self.answer}"

    @property
    def score(self):
        return 1/self.last_used

    @property
    def last_used(self):
        return self._last_used

    @last_used.setter
    def last_used(self, val):
        self._last_used = val


class BasicQuestionWithStatistics(BasicQuestion):
    def __init__(self, question: str = None, answer: str = None, stats_raw: str = None, score_stat: bool = True):
        """ Creates the question.

            :param stats_raw; if not None, it loads them with StatisticsLoader.
            :param score_stat;   if True it adds score statistics to the holder.
                            This options is ignored if 'stats_raw is not None'.
        """
        self.stats_holder = StatisticsHolder()
        if stats_raw is not None:
            self.stats_holder.build_from_string(stats_raw)
        else:
            if score_stat:
                self.stats_holder.add_statistics("score", ScoreStatistics())
        self.score_stat = score_stat
        super().__init__(question, answer)

    def __str__(self):
        return f"{self.question},{self.answer},{self.stats_holder.dump()}"

    @property
    def score(self):
        if self.score_stat:
            return (self.stats_holder["score"].correct + 1) / (self.stats_holder["score"].total + 1 + self.last_used / 10)
        return 0
