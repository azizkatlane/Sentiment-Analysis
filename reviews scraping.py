
import requests
from bs4 import BeautifulSoup
import pandas as pd
from textblob import TextBlob


page = requests.get("https://www.imdb.com/title/tt2935510/reviews?ref_=tt_urv")
soup = BeautifulSoup(page.content, "html.parser")
rev = soup.findAll('div', class_='text show-more__control')
movies = []
for movie in rev:
    movies.append(movie.text)
df = pd.DataFrame(
    {'reviews': movies}

     )


list=[]
for i in range(len(movies)):
    text=TextBlob(movies[i])
    x=text.sentiment.polarity # x between -1 and 1
    list.append(round(x,2))
list


sent=[]
j=[]
for j in list:
    if j>0:
        x="positive"
    elif j==0:
        x="neutre"
    else :
        x="negative"
    sent.append(x)


df['sentiment']=sent
print(df)

