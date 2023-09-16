# https://www.codewars.com/kata/6089c7992df556001253ba7d

class Song():
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.already_listed = set()
        
    def how_many(self, listeners):
        cnt_before = len(self.already_listed)
        self.already_listed = self.already_listed.union(set(map(str.lower, listeners)))
        return (len(self.already_listed) - cnt_before)
