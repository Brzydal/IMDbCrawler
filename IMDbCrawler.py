import requests
from bs4 import BeautifulSoup


# Spider will get a list of how many first movies from IMDb you want

def id_spider(url,how_many):
    result = []
    page_text = requests.get(url).text
    soup = BeautifulSoup(page_text,"lxml")
    movies = soup.findAll('td',{'class':'titleColumn'})

    for movie in movies:
        number = movie.text.split('.')[0]
        links = movie.findAll('a')
        for a in links:
            href = a.get('href')
            movie_id = parse_movie_id(href)
        if int(number) <= how_many:
            result.append(movie_id)

    return result

# This little parser will get a movie id from a href

def parse_movie_id(href):
    movie_id = href.split('/')[2]
    return(movie_id)

# This spider will get a movie details by id from omdbapi

def details_spider(url,id_list):





list_of_id = id_spider('http://www.imdb.com/chart/top?ref=ft_250',100)
details_spider('http://www.omdbapi.com/?i',list_of_id)

# I dont know if it was a part of the test but I have noticed that We could get title and year directly from td