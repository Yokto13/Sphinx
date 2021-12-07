import unittest
from statistics_builder import StatisticsBuilder
from statistics import ScoreStatistics
from custom_errors import UnknownStatisticsTypeError
from questions import BasicQuestion, BasicQuestionWithStatistics


class StatisticsBuilderTestCase(unittest.TestCase):
    def test_build_wrong(self):
        with self.assertRaises(UnknownStatisticsTypeError):
            sep = StatisticsBuilder.separator
            StatisticsBuilder.build("non-existent type!!" + sep + "body of stat")

    def test_build_score_correct(self):
        dumped1 = f"score{StatisticsBuilder.separator}1,2"
        score, stat = StatisticsBuilder.build(dumped1)
        stat2 = ScoreStatistics()
        stat2.correct = 1
        stat2.total= 2
        self.assertEqual(stat, stat2)
        self.assertEqual(score, "score")

    def test_build_wrong_raw(self):
        with self.assertRaises(ValueError):
            score, stat = StatisticsBuilder.build("2")
        with self.assertRaises(ValueError):
            score, stat = StatisticsBuilder.build(f"{StatisticsBuilder.separator}" * 5)


class ScoreStatisticsTestCase(unittest.TestCase):
    def test_defaults(self):
        stat = ScoreStatistics()
        self.assertEqual(stat.total, 0)
        self.assertEqual(stat.correct, 0)

    def test_update(self):
        stat = ScoreStatistics()
        for i in range(10):
            stat.update(False)
            self.assertEqual(stat.total, i + 1)
        for i in range(10):
            stat.update(True)
            self.assertEqual(stat.total, i + 10 + 1)
            self.assertEqual(stat.correct, i + 1)

    def test_str(self):
        stat = ScoreStatistics()
        self.assertEqual(str(stat), "0 correct from 0 total.")
        for i in range(10):
            stat.update(False)
            self.assertEqual(stat.total, i + 1)
        stat.update(True)
        self.assertEqual(str(stat), "1 correct from 11 total.")

    def test_dump_load(self):
        stat = ScoreStatistics()
        self.assertEqual(ScoreStatistics(stat.dump()), stat)
        for i in range(10):
            stat.update(i & 1)
        self.assertEqual(ScoreStatistics(stat.dump()), stat)

    def test_eq(self):
        stat = ScoreStatistics()
        self.assertTrue(stat == stat)
        stat1 = ScoreStatistics()
        self.assertTrue(stat == stat1)
        stat1.update(False)
        self.assertFalse(stat == stat1)
        stat.update(False)
        self.assertTrue(stat == stat1)


class BasicQuestionTestCase(unittest.TestCase):
    def test_creation(self):
        """ Ultra simple test just checking if BQ is created as expected. """
        q = "What is the temperature of water in Bolevak?"
        a = "2.5"
        bq = BasicQuestion(q, a)
        self.assertEqual(bq.question, q)
        self.assertEqual(bq.answer, a)


class BasicQuestionWithStatisticsTestCase(unittest.TestCase):
    def test_creation(self):
        """ Ultra simple test just checking if BQwS is created as expected. """
        q = "What is the temperature of water in Bolevak?"
        a = "2.5"
        bq = BasicQuestionWithStatistics(q, a, score=True)
        self.assertEqual(bq.question, q)
        self.assertEqual(bq.answer, a)
        self.assertEqual(bq.stats_holder["score"].total, 0)
        self.assertEqual(bq.stats_holder["score"].correct, 0)


if __name__ == '__main__':
    unittest.main()
