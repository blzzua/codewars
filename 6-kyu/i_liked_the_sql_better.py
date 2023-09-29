# https://www.codewars.com/kata/53d2c97d7152a59b64001033

import sqlite3

conn = sqlite3.connect('/tmp/movies.db')
cur = conn.cursor()
cur.execute("""create table MOVIES (Id integer,  Name varchar(100), Year integer, Rating integer)""")
conn.commit()
data = [(1, 'Rise of the Planet of the Apes', 2011, 77),
  (2, 'Dawn of the Planet of the Apes', 2014, 91),
  (3, 'Alien', 1979, 97),
  (4, 'Aliens', 1986, 98),
  (5, 'Mad Max', 1979, 95),
  (6, 'Mad Max 2: The Road Warrior', 1981, 100)]
cur.executemany('INSERT INTO MOVIES VALUES (?, ?, ?, ?)', data)
conn.commit()
cur.execute('select Name, Year, Rating from MOVIES order by Id')
result = cur.fetchall()
conn.close()
return result
