from unittest import TestCase
from main import Plugboard

class TestPlugboard(TestCase):
    def test_swap(self):
        plugboard = Plugboard("ABCDEFGHIJKLMNOPQRST")
        # alphabets we want to change
        self.assertEqual(plugboard.swap('A'), 'B')
        self.assertEqual(plugboard.swap('B'), 'A')
        self.assertEqual(plugboard.swap('C'), 'D')
        self.assertEqual(plugboard.swap('D'), 'C')
        # alphabets not to be changed
        self.assertEqual(plugboard.swap('Y'), 'Y')

if __name__ == '__main__':
    from unittest import main
    main()