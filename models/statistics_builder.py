""" Builds statistics from strings. """
from .custom_errors import UnknownStatisticsTypeError
from .statistics import ScoreStatistics
from .abstract_statistics import AbstractStatistcs


class StatisticsBuilder:
    separator = "?|?|?"

    @classmethod
    def build(cls, raw: str) -> AbstractStatistcs:
        """ Builds single statistics. """
        stat_type, body = raw.split(cls.separator)
        if stat_type == "score":
            return stat_type, ScoreStatistics(body)
        else:
            raise UnknownStatisticsTypeError
