# https://www.codewars.com/kata/5a57d101cadebf03d40000b9

from bs4 import BeautifulSoup
import requests

def get_leaderboard_honor():
    url='https://www.codewars.com/users/leaderboard'
    r = requests.get(url=url)
    html = r.text
    soup = BeautifulSoup(html)
    leaderboard = soup.find('div', class_='leaderboard')
    honor= leaderboard.find('table').find_all('td', class_='honor')
    res = [int(h.text.replace(',','')) for h in honor]
    return res

