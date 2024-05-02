# https://www.codewars.com/kata/5631ac5139795b281d00007d

import re
class WordDictionary:
    def __init__(self):
        self.list=set()

    def add_word(self, word):
        self.list.add(word)

    def search(self, pattern):
        print(pattern)
        for word in self.list:
            if bool(re.match(r'^'+pattern+'$', word)):
                return True
        return False
