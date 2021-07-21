import pyautogui

words = open('words', 'r')
words_list = [word[:-1] for word in words]


class Hive:
    """A solver for the New York Times' Spelling Bee.
    Takes the outer letters and center letter as parameters,
    then solves the puzzle."""

    def __init__(self, outer_letters, center_letter):
        self.outer_letters = outer_letters
        self.center_letter = center_letter
        self.all_letters = outer_letters + list(center_letter)
        self.solutions = []

    def _find_words(self):

        """Checks if the center letter is in the word, if the word has been found,
        and if the word has 4 or more letters, then compares the set of the word to the set of letters.
        If it passes all tests, the word is added to the list of solutions."""

        for word in words_list:
            if self.center_letter in word:
                if word not in self.solutions:
                    if len(word) > 3:
                        if set(word) <= set(self.all_letters):
                            self.solutions.append(word)

    def list_words(self):
        """Prints words in a neatly formatted list"""
        self._find_words()
        for word in self.solutions:
            print(f'|-> {word} <-|')

    def _type_solutions(self):
        """Uses PyAutoGUI to type out the words into the prompter on the Queen Bee website."""
        pyautogui.sleep(5)
        for word in self.solutions:
            pyautogui.typewrite(word)
            pyautogui.press('enter')
    
    def solve(self):
        """Finds every word, then types out the word."""
        self._find_words()
        self._type_solutions()


outer = ['b', 'i', 'h', 'c', 'o', 'n']
center = 'r'

hive = Hive(outer, center)

hive.solve()
