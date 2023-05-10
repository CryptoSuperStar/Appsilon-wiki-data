import requests
import sqlite3


url = 'https://query.wikidata.org/sparql'
query = '''
SELECT DISTINCT ?movie ?movieLabel ?imdbID ?releaseDate
WHERE {
  ?movie wdt:P31 wd:Q11424;
         wdt:P577 ?releaseDate;
         wdt:P345 ?imdbID.
  FILTER(YEAR(?releaseDate) > 2013)
         
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
'''
conn = sqlite3.connect('movie.db')
cursor = conn.cursor()
cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='movies'")
table = cursor.fetchone()
if not(table):
    cursor.execute('''CREATE TABLE movies
                    (id INTEGER PRIMARY KEY,
                    movieLabel TEXT,
                    imdb_id TEXT,
                    release_date TEXT,
                    movie TEXT
                    )''')


response = requests.get(url, params={'query': query, 'format': 'json'})

if response.status_code == 200:
    data = response.json()
    results = data['results']['bindings']
    for result in results:
        cursor.execute('''SELECT * FROM movies WHERE imdb_id = ?''', (result['imdbID']['value'],))
        selectedData = cursor.fetchone()
        if selectedData:
            cursor.execute('''UPDATE movies SET movieLabel = ?, release_date = ?, movie = ?
                  WHERE imdb_id=?''', (result['movieLabel']['value'], result['releaseDate']['value'], result['movie']['value'], result['imdbID']['value']))
        else:
            cursor.execute('''INSERT INTO movies (movieLabel, imdb_id, release_date, movie)
                  VALUES (?, ?, ?, ?)''', (result['movieLabel']['value'], result['imdbID']['value'], result['releaseDate']['value'], result['movie']['value']))
    conn.commit()
    cursor.close()
    conn.close()
else:
    print('Failed with status code:', response.status_code)
