import numpy as np
# I  hardcoded all the rotor wiring settings 
class Rotor:
    # Rotor number matching to tuple (wiring's,notch position)
    Rotor_wirings = {
        1: ("EKMFLGDQVZNTOWYHXUSPAIBRCJ", "Q"),
        2: ("AJDKSIRUXBLHWTMCQGZNPYFVOE", "E"),
        3: ("BDFHJLCPRTXVZNYEIWGAKMUSQO", "V"),
        4: ("ESOVPZJAYQUIRHXLNFTGKDCMWB", "J"),
        5: ("VZBRGITYUPSDNHLXAWMJQOFECK", "Z")
    }

    def __init__(self, rotor_num, position):
        self.rotor_num = rotor_num
        self.wiring, self.notch = self.Rotor_wirings[rotor_num]
        self.position = position
        self.wiring = np.array(list(self.wiring))
        self.alphabet = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def rotate(self):
        self.position = (self.position + 1) % 26
    #used CoPilot prompt-find the index for a letter based on the rotor's current position in the array
    #new index for a letter based on the rotor's position and then returns the mapped letter from the rotor wiring
    def encode_forward(self, letter):
        #np.where returns a tuple with an array of indices
        # then extracts the first matching index, which corresponds to the letter position in the alphabet
        # then shift letter index forward by the rotor’s position
        index = (np.where(self.alphabet == letter)[0][0] + self.position) % 26
        return self.wiring[index]

    def encode_backward(self, letter) :
        index = np.where(self.wiring == letter)[0][0]
        index = (index - self.position) % 26
        return self.alphabet[index]

class Reflector:
    def __init__(self):
        self.wiring = np.array(list("YRUHQSLDPXNGOKMIEBFZCWVJAT"))
        self.alphabet = np.array(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

    def reflect(self, letter) :
        index = np.where(self.alphabet == letter)[0][0]
        return self.wiring[index]

class Plugboard:
    def __init__(self, swaps):
        self.swaps = {}
        for i in range(0, len(swaps), 2):
            self.swaps[swaps[i]] = swaps[i + 1]
            self.swaps[swaps[i + 1]] = swaps[i]

    # swaps the letter if it's in the plugboard settings(in the dictionary)
    def swap(self, letter) :
        return self.swaps.get(letter, letter)

class EnigmaMachine:
    def __init__(self, rotor_nums, positions, plugboard_settings):
        self.rotors = [Rotor(rotor_nums[i], positions[i]) for i in range(3)]
        self.reflector = Reflector()
        self.plugboard = Plugboard(plugboard_settings)

    def step_rotors(self):
        #rightmost rotor always rotates when a key is pressed
        rotate_next = True
        for rotor in self.rotors:
            if rotate_next:
                rotor.rotate()
                rotate_next = (rotor.position == (np.where(rotor.alphabet == rotor.notch)[0][0]))
            else:
                break

    def encrypt_letter(self, letter) :
        self.step_rotors()
        letter = self.plugboard.swap(letter)

        # forward through rotors
        for rotor in self.rotors:
            letter = rotor.encode_forward(letter)

        # reflection
        letter = self.reflector.reflect(letter)

        # backward through rotors
        for rotor in reversed(self.rotors):
            letter = rotor.encode_backward(letter)

        return self.plugboard.swap(letter)
    # looked up on AI how to join letters without separator
    def encrypt_message(self, message) :
        encrypted_message = ''.join(self.encrypt_letter(letter) for letter in message if letter.isalpha())
        return encrypted_message


def main():
    print(" ***ENIGMA MACHINE*** ")
    # User selects rotors
    rotor_nums = list(map(int, input("Enter rotor numbers : 3 numbers from 1-5): ")))
    positions = list(map(int, input("Enter notch positions for each rotor-3 numbers between 0-25): ")))
    plugboard_settings = input("Enter 20-character plugboard settings ( ABCDEFGHIJKLMNOPQRST): ").upper()

    enigma = EnigmaMachine(rotor_nums, positions, plugboard_settings)
    mode = input("Encrypt or Decrypt a message? (E/D): ").upper()
    while mode not in ["E", "D"]:
        mode = input("Invalid choice. Enter 'E' for Encrypt or 'D' for Decrypt: ").upper()

    message = input("Enter message with no spaces : ").upper()

    if mode == "E":
        result = enigma.encrypt_message(message)
    else:
        result = enigma.encrypt_message(message)

    print(f"\n{'Encrypted' if mode == 'E' else 'Decrypted'} Message: {result}")

if __name__ == "__main__":
    main()