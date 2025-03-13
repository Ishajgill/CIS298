import unittest
from main import Rotor

class TestRotor(unittest.TestCase):
    def test_rotate(self):
        rotor = Rotor(1, position=0)
        rotor.rotate()
        self.assertEqual(rotor.position, 1)
        #check if it wraps around after last alphabet(z)
        rotor.position = 25
        rotor.rotate()
        self.assertEqual(rotor.position, 0)

    def test_encode_forward(self):
        rotor = Rotor(1, position=0)
        encoded = rotor.encode_forward('A')
        self.assertEqual(encoded, 'E')

    def test_encode_backward(self):
        rotor = Rotor(1, position=0)
        decoded = rotor.encode_backward('E')
        self.assertEqual(decoded, 'A')


if __name__ == '__main__':
    unittest.main()
