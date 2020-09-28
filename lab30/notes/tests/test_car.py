import unittest
from car import Car


class TestMyCar(unittest.TestCase):
    def setUp(self):
        self.c1 = Car('blue', 20)
        self.c2 = Car('green', 30)

    def test_faster_than(self):
        self.assertTrue(self.c2.is_faster_than(self.c1))


if __name__ == '__main__':
    unittest.main()
