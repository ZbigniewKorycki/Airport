import unittest
from airplane import Airplane


class TestAirplane(unittest.TestCase):

    def setUp(self):
        self.airplane = Airplane()

    def tearDown(self):
        pass

    def test_get_starting_position(self):
        starting_position = self.airplane.get_starting_position()
        self.assertEqual(3, len(starting_position))
        self.assertGreaterEqual(5000, starting_position[2])
        self.assertLessEqual(2000, starting_position[2])
        self.assertGreaterEqual(10000, starting_position[0])
        self.assertLessEqual(0, starting_position[0])
        self.assertGreaterEqual(10000, starting_position[1])
        self.assertLessEqual(0, starting_position[1])

