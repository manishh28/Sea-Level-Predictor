import unittest

from sea_level_predictor import draw_plot


class SeaLevelPredictorTestCase(unittest.TestCase):
    def test_plot_labels_and_lines(self):
        axis = draw_plot()
        self.assertEqual(axis.get_title(), "Rise in Sea Level")
        self.assertEqual(axis.get_xlabel(), "Year")
        self.assertEqual(axis.get_ylabel(), "Sea Level (inches)")
        self.assertEqual(len(axis.lines), 2)


if __name__ == "__main__":
    unittest.main()
