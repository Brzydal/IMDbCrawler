import requests
from bs4 import BeautifulSoup
import csv

# Mother of spiders sent her kids to gather info and save it in a file
def spiders_mum(url,how_many,file_name):
    id_list = id_spider(url,how_many)
    movies_dict = details_spider(id_list)
    saving_spider(file_name,movies_dict)

# Spider will get a list of movies from IMDb (how many first movies you want)
def id_spider(url,how_many):
    result = []
    page_text = requests.get(url).text
    soup = BeautifulSoup(page_text)
    movies = soup.findAll('td',{'class':'titleColumn'})

    for movie in movies:
        number = movie.text.split('.')[0]
        links = movie.findAll('a')
        for a in links:
            href = a.get('href')
            movie_id = parseing_spider(href)
        if int(number) <= how_many:
            result.append(movie_id)

    return result

# This little parser will get a movie id from a href

def parseing_spider(href):
    movie_id = href.split('/')[2]
    return(movie_id)

# This spider will get a movies details by id from omdbapi and put them into dictionary {Title : Year}

def details_spider(id_list):
    result = {}
    for id in id_list:
        response = requests.get('http://www.omdbapi.com/?i='+id)
        result[response.json()['Title']] = response.json()['Year']
    return result

# This function will sort results and save to csv file

def saving_spider(file_name,movies_dict):
    with open(file_name, 'w') as f:
        w = csv.writer(f)
        w.writerows(sorted(movies_dict.items(), key=lambda x: x[1]))

# I dont know if it was a part of the test but I have noticed that We could get title and year directly from td

# Black_Widow = spiders_mum('http://www.imdb.com/chart/top?ref=ft_250', 100, 'movies.csv')