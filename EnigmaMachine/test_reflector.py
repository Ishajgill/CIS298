from unittest import TestCase
from main import Reflector

class TestReflector(TestCase):
    def test_reflect(self):
        reflector = Reflector()

        self.assertEqual(reflector.reflect('A'), 'Y')  # A to Y
        self.assertEqual(reflector.reflect('Y'), 'A')  # Y to A
        self.assertEqual(reflector.reflect('B'), 'R')  # B to R
        self.assertEqual(reflector.reflect('R'), 'B')  # R to B
        #  bidirectional
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            reflected_letter = reflector.reflect(letter)
            self.assertEqual(reflector.reflect(reflected_letter), letter)

if __name__ == '__main__':
    from unittest import main
    main()
