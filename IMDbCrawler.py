import requests
from bs4 import BeautifulSoup
import csv


def spiders_mum(url, how_many, file_name):
    """
    Mother of spiders sent her kids to gather info and save it in a file

    :param url:
    :param how_many:
    :param file_name:
    """
    id_list = id_spider(url, how_many)
    print('ID List has {} elements'.format(len(id_list)))
    movies_dict = details_spider(id_list)
    print('Movies details in dictionary')
    saving_spider(file_name, movies_dict)
    print('{} has been created'.format(file_name))


def id_spider(url, how_many):
    """
    Spider will get a list of movies from IMDb (how many first movies you want)
    :param url:
    :param how_many:
    :return: result - list of movies id
    """

    movie_id = None
    result = []
    page_text = requests.get(url).text
    soup = BeautifulSoup(page_text)
    movies = soup.findAll('td', {'class': 'titleColumn'})

    for movie in movies:
        number = movie.text.split('.')[0]
        links = movie.findAll('a')
        for a in links:
            href = a.get('href')
            movie_id = parsing_spider(href)
        if int(number) <= how_many:
            result.append(movie_id)

    return result


def parsing_spider(href):
    """
    # This little parser will get a movie id from a href
    :param href:
    :return: movie id
    """
    movie_id = href.split('/')[2]
    return movie_id


def details_spider(id_list):
    """
    This spider will get a movies details by id from omdbapi and put them into dictionary {Title : Year}
    :param id_list:
    :return: result - dictionary where titles are keys and Years of release are Values
    """

    result = {}
    for movie_id in id_list:
        response = requests.get('http://www.omdbapi.com/?i=' + movie_id)
        result[response.json()['Title']] = response.json()['Year']
    return result


def saving_spider(file_name, movies_dict):
    """
    # This function will sort results and save to csv file
    :param file_name:
    :param movies_dict:
    :return:
    """

    with open(file_name, 'w') as f:
        w = csv.writer(f)
        w.writerows(sorted(movies_dict.items(), key=lambda x: x[1]))


if __name__ == "__main__":
    print ("### Starting Spider! ###")
    Black_Widow = spiders_mum('http://www.imdb.com/chart/top?ref=ft_250', 100, 'movies.csv')
    print ("### Spider has left... ###")
