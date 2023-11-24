import unittest
from airplane import Airplane


class TestAirplane(unittest.TestCase):

    def setUp(self):
        self.airplane = Airplane()

    def tearDown(self):
        pass

    def test_get_starting_position(self):
        starting_position = self.airplane.get_starting_position()
        self.assertIn("x", starting_position)
        self.assertIn("y", starting_position)
        self.assertIn("z", starting_position)
        self.assertEqual(3, len(starting_position))
        self.assertGreaterEqual(5000, starting_position["z"])
        self.assertLessEqual(2000, starting_position["z"])
        self.assertGreaterEqual(10000, starting_position["x"])
        self.assertLessEqual(0, starting_position["x"])
        self.assertGreaterEqual(10000, starting_position["y"])
        self.assertLessEqual(0, starting_position["y"])

