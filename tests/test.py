import unittest
import power_index_calculator as calculator


class TestPowerIndices(unittest.TestCase):
    """
    TODO
    """
    def test_banzhaf(self):
        """
        TODO
        """
        g1 = [3, 3, 5, 5, 7, 16, 47, 9, 11, 18, 11, 5, 9, 3, 3]

        q1 = 89

        r = [0.017, 0.017, 0.028, 0.028, 0.039,
             0.089, 0.396, 0.051, 0.062, 0.1,
             0.062, 0.028, 0.051, 0.017, 0.017]

        res = list(calculator.banzhaf(g1, q1))
        self.assertEqual(res, r)

    def test_deegan_packel(self):
        """
        TODO
        """
        g1 = [3, 3, 5, 5, 7, 16, 47, 9, 11, 18, 11, 5, 9, 3, 3]

        q1 = 89

        r = [0.06, 0.06, 0.064, 0.064, 0.064, 0.059,
             0.131, 0.065, 0.065, 0.056, 0.065, 0.064,
             0.065, 0.06, 0.06]

        res = list(calculator.deegan_packel(g1, q1))
        self.assertEqual(res, r)

    def test_shapley(self):
        """
        TODO
        """
        g1 = [3, 3, 5, 5, 7, 16, 47, 9, 11, 18, 11, 5, 9, 3, 3]

        q1 = 89

        r = [0.016, 0.016, 0.028, 0.028, 0.039, 0.091,
             0.393, 0.051, 0.062, 0.103, 0.062, 0.028,
             0.051, 0.016, 0.016]

        res = list(calculator.shapley(g1, q1))
        self.assertEqual(res, r)


if __name__ == '__main__':
    unittest.main()
