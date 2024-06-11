# https://www.codewars.com/kata/581c06b95cfa838603000435

from bs4 import BeautifulSoup
import requests

URL = "https://www.codewars.com/users/leaderboard"

class User:
    def __init__(self, tr):
        """ tr: bs4 element html tag <tr>...</tr> """
        self.name = tr["data-username"]
        self.rank = int(tr.find('td', class_="rank").text.strip('#'))
        self.honor = int(tr.find('td', class_="honor").text.replace(',',''))
        self.clan = tr.find('td', class_="honor").find_previous_sibling('td').text

class Leaderboard:
        def __init__(self):
            self._list = []
            self.__len__ = self._list.__len__
            self.position = {}
            
        def append(self, item):
            self._list.append(item)
            if item.rank in self.position:      #  TODO workaround only for 2 users, which have same rank in leaderboard. Will not work for 3 and more. 
                self.position[item.rank+1] = item
            else:
                self.position[item.rank] = item
           
            
def solution():
    r = requests.get(url=URL)
    html = r.text
    soup = BeautifulSoup(html)
    bs4_leaderboard = soup.find('div', class_='leaderboard')
    users = bs4_leaderboard.find('table').find_all('tr')
    leaderboard = Leaderboard()
    for tr in users[1:]:       # 0-nth element is header
        leaderboard.append(User(tr))
    return leaderboard
