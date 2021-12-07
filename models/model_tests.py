import unittest
from statistics_builder import StatisticsBuilder
from score_statistics import ScoreStastics
from custom_errors import UnknownStatisticsTypeError


class StatisticsBuilderTestCase(unittest.TestCase):
    def test_build_wrong(self):
        with self.assertRaises(UnknownStatisticsTypeError):
            sep = StatisticsBuilder.separator
            StatisticsBuilder.build("non-existent type!!" + sep + "body of stat")

    def test_build_correct(self):
        raise NotImplementedError


class ScoreStatisticsTestCase(unittest.TestCase):
    def test_defaults(self):
        stat = ScoreStastics()
        self.assertEqual(stat.total, 0)
        self.assertEqual(stat.correct, 0)

    def test_update(self):
        stat = ScoreStastics()
        for i in range(10):
            stat.update(False)
            self.assertEqual(stat.total, i+1)
        for i in range(10):
            stat.update(True)
            self.assertEqual(stat.total, i+10+1)
            self.assertEqual(stat.correct, i+1)

    def test_str(self):
        stat = ScoreStastics()
        self.assertEqual(str(stat), "0 correct from 0 total.")
        for i in range(10):
            stat.update(False)
            self.assertEqual(stat.total, i+1)
        stat.update(True)
        self.assertEqual(str(stat), "1 correct from 11 total.")


    def test_dump_load(self):
        raise NotImplementedError

    def test_eq(self):
        stat = ScoreStastics()
        self.assertTrue(stat == stat)
        stat1 = ScoreStastics()
        self.assertTrue(stat == stat1)
        stat1.update(False)
        self.assertFalse(stat == stat1)
        stat.update(False)
        self.assertTrue(stat == stat1)


if __name__ == '__main__':
    unittest.main()
