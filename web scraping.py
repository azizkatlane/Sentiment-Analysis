import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

url = requests.get('https://www.imdb.com/list/ls026827286/')
url.raise_for_status()

soup = BeautifulSoup(url.content, "html.parser")

titles = []
years = []
ratings = []
genres = []
runtimes = []
metascores = []
votes = []

movies = soup.findAll('div', attrs={'class': 'lister-item mode-detail'})
for movie in movies:
    title = movie.h3.a.text
    titles.append(title)

    year = movie.find('span', attrs={'class': 'lister-item-year text-muted unbold'}).text.replace('(', '').replace(')',
                                                                                                                   '')
    years.append(year)

    rating = movie.find('span', attrs={'class': 'ipl-rating-star__rating'}).text
    ratings.append(rating)

    genre = movie.find('span', attrs={'class': 'genre'}).text.replace('\n', '').rstrip().split(',')
    genres.append(genre)

    runtime = movie.find('span', attrs={'class': 'runtime'}).text
    runtimes.append(runtime)

    metascore = int(movie.find('span', attrs={'class': 'metascore'}).text)
    metascores.append(metascore)

    value = movie.find_all('span', attrs={'name': 'nv'})

    vote = value[0].text
    votes.append(vote)

movie_df = pd.DataFrame({'movie': titles,
                         'year': years,
                         'rating': ratings,
                         'genre': genres,
                         'runtime_min': runtimes,
                         'metascore': metascores,
                         'votes': votes,
                         }
                        )

print(movie_df)
