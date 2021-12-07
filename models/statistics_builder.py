from custom_errors import UnknownStatisticsTypeError


class StatisticsBuilder:
    separator = "?|?|?"

    @classmethod
    def build(cls, raw: str):
        stat_type, body = raw.split(cls.separator)
        if stat_type == "score":
            pass
        else:
            raise UnknownStatisticsTypeError
