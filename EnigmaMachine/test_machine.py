from unittest import TestCase
from main import EnigmaMachine

class TestEnigmaMachine(TestCase):
    def test_step_rotors(self):
        enigma = EnigmaMachine([1, 2, 3], [0, 0, 0], "ABCDEFGHIJKLMNOPQRST")
        enigma.step_rotors()
        # only rightmost rotor should move
        self.assertEqual(enigma.rotors[0].position, 1)
        self.assertEqual(enigma.rotors[1].position, 0)
        self.assertEqual(enigma.rotors[2].position, 0)
        # second rotor should move, notch position for rotor 1  is 16('Q')
        enigma.rotors[0].position = 15
        enigma.step_rotors()
        self.assertEqual(enigma.rotors[0].position, 16)
        self.assertEqual(enigma.rotors[1].position, 1)
        self.assertEqual(enigma.rotors[2].position, 0)

    def test_encrypt_message(self):
        enigma = EnigmaMachine([1, 2, 3], [0, 0, 0], "ABCDEFGHIJKLMNOPQRST")
        original_message = "HELLO"
        encrypted_message = enigma.encrypt_message(original_message)
        self.assertNotEqual(encrypted_message, original_message)
        self.assertEqual(len(encrypted_message), len(original_message))
        self.assertTrue(encrypted_message.isalpha())
        # reversible
        enigma = EnigmaMachine([1, 2, 3], [0, 0, 0], "ABCDEFGHIJKLMNOPQRST")
        decrypted_message = enigma.encrypt_message(encrypted_message)
        self.assertEqual(decrypted_message, original_message)

if __name__ == '__main__':
    from unittest import main
    main()
