""" Holds are statistics for some question and manages them.

    One question might have multiple statistics (for example time, correctness...).
"""
from typing import Dict
from abstract_statistics import AbstractStatistcs
from statistics_builder import StatisticsBuilder


class StatisticsHolder:
    def __init__(self):
        self._statistics: Dict[str, AbstractStatistcs] = {}
        self.stat_stat_separator = ";|;|;"
        self.type_stat_separator = StatisticsBuilder.separator

    def add_statistics(self, key: str, stat: AbstractStatistcs):
        if key in self._statistics:
            raise LookupError
        else:
            self._statistics[key] = stat

    def remove_statistics(self, key: str):
        del self._statistics[key]

    def build_from_string(self, dump_of_holder: str):
        raw_statistics = dump_of_holder.split(self.separator)
        for raw in raw_statistics:
            stat_type, stat = StatisticsBuilder.build(raw)
            self.add_statistics(stat_type, stat)

    def dump(self) -> str:
        res = []
        for stat_type, stat in self._statistics.items():
            res.append(stat_type + self.type_stat_separator + stat.dump())
        return self.stat_stat_separator.join(res)
