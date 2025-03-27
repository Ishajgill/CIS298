import random

class Hangman:
    common_words = [
        "apple", "banana", "grape", "orange", "strawberry",
        "elephant", "giraffe", "kangaroo", "lion", "tiger",
        "computer", "keyboard", "mouse", "monitor", "printer",
        "python", "java", "javascript", "html", "css",
        "mountain", "river", "ocean", "forest", "desert",
        "happy", "sad", "angry", "excited", "bored"
    ]

    def __init__(self):
        self._word_to_guess = random.choice(self.common_words).upper()
        self._number_of_incorrect_guesses = 0
        self._letters_guessed = []

    def guess_letter(self, letter):
        if letter in self._letters_guessed:
            return ""
        self._letters_guessed.append(letter)
        if letter not in self._word_to_guess:
            self._number_of_incorrect_guesses += 1

    def get_word_to_guess(self):
        return self._word_to_guess

    def game_over(self):
        if self._number_of_incorrect_guesses == 6:
            return True
        for letter in self._word_to_guess:
            if letter not in self._letters_guessed:
                return False
        return True

    def get_number_of_incorrect_guesses(self):
        return self._number_of_incorrect_guesses

    def get_display(self):
        result = ""
        for letter in self._word_to_guess:
            if letter in self._letters_guessed:
                result += letter + " "
            else:
                result += "_ "
        return result

    def get_letters_guessed(self):
        return self._letters_guessed[:]