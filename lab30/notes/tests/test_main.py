import unittest
from unittest.mock import MagicMock, patch
from main import main
from io import StringIO


class TestMain(unittest.TestCase):


    def test_red_car_is_faster(self):
        fake_input = MagicMock()
        fake_input.side_effect = ['40', '60']
        fake_output = StringIO()

        with patch('builtins.input', fake_input), patch('sys.stdout', fake_output):
            main()
            self.assertEqual('And the winner is... blue car\n', fake_output.getvalue())


if __name__ == '__main__':
    unittest.main()
