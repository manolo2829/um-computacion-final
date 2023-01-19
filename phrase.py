
from word import Word

class Phrase:

    def __init__(self):
        self.sequence = []

    def __repr__(self):
        return self.sequence


    def encode(self, phrase):
        wordList = phrase.split()
        for wordItem in wordList:
            word = Word()
            result_word = word.encode(wordItem)
            self.sequence.append(result_word)
        text = f"{self.sequence}"
        text = text.replace('"', '')
        text = text.replace("'", '')
        self.sequence = text
