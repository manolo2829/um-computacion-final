
class Word:

    def __init__(self):
        self.listLetter = []  
        self.objLetter = {}
        self.position = 0

    def encode(self, word):
        for letter in word:
            self.position += 1
            if not letter in self.listLetter:
                self.objLetter[letter] = [self.position] 
                self.listLetter.append(letter) 
            else:
                newList = self.objLetter[letter]
                newList.append(self.position)
                self.objLetter[letter] = newList
        text = f"{self.objLetter}"
        newText = text.replace('{', '[')
        newText = newText.replace('}', ']')
        return newText