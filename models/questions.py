from .abstract_question import AbstractQuestion
from .statistics_holder import StatisticsHolder
from .statistics import ScoreStatistics


class BasicQuestion(AbstractQuestion):
    def __init__(self, question=None, answer=None):
        self._question: str = question
        self._answer: str = answer
        self._score = 0

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
        return self._score


class BasicQuestionWithStatistics(BasicQuestion):
    def __init__(self, question: str = None, answer: str = None, stats_raw: str = None, score_stat: str = True):
        """ Creates the question.

            :param stats_raw; if not None, it loads them with StatisticsLoader.
            :param score;   if True it adds score statistics to the holder.
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
            return (self.stats_holder["score"].correct + 1) / (self.stats_holder["score"].total + 1)
        return 0
