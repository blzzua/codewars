# https://www.codewars.com/kata/57a93f93bb9944516d0000c1

class Dictionary():
    def __init__(self):
        self.data = {}
        
    def newentry(self, word, definition):
        self.data[word] = definition
        
    def look(self, key):
        return self.data.get(key, f"Can't find entry for {key}")
