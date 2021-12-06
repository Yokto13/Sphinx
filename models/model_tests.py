import unittest
from statistics_builder import StatisticsBuilder
from custom_errors import UnknownStatisticsTypeError


class StatisticsBuilderTestCase(unittest.TestCase):
    def test_build_wrong(self):
        with self.assertRaises(UnknownStatisticsTypeError):
            sep = StatisticsBuilder.separator
            StatisticsBuilder.build("non-existent type!!" + sep + "body of stat")

    def test_build_correct(self):
        raise NotImplementedError

if __name__ == '__main__':
    unittest.main()
