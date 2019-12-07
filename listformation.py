from bs4 import BeautifulSoup
import requests

class extract:
    source=requests.get('https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc').text
    soup=BeautifulSoup(source, 'lxml')
    m=[]
    for movie in soup.find_all('div', class_='lister-item-content'):
        
        movie_name=movie.h3.a.text
        m.append(movie_name)
    # print(m)

    # print()
    y=[]
    for year in soup.find_all('span', class_='lister-item-year text-muted unbold'):
        year_brack=year.text
        year_brack=year_brack.strip('()')
        year_int=int(year_brack)
        y.append(year_int)
        #print(year_int)
    # print(y)
    # print()

    r=[]
    for runtime in soup.find_all('span', class_='runtime'):
        runtime_min=runtime.text
        runtime_no_min=runtime_min.strip(' min')
        runtime_int=int(runtime_no_min)
        r.append(runtime_int)
    # print(r)
    # print()
    splt=[]
    sp=[]
    for genre in soup.find_all('span', class_='genre'):
        genre_space=genre.text
        gene=genre_space.strip()
        splt=gene.split(", ")
        sp.append(splt)

    # print(sp)
    s=[]
    for genre in soup.find_all('div', class_='ratings-bar'):
        IMDB_Rate=genre.strong.text
        IMDBRate=float(IMDB_Rate)
        s.append(IMDBRate)
    # print(s)
    