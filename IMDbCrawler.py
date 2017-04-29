import requests
from bs4 import BeautifulSoup
import csv


class Spider():

    # A Spider which will gather information about 'n' movies from website (IMDb) and save it in a file

    url = 'http://www.imdb.com/chart/top?ref=ft_250'
    how_many_movies_ = 100
    output_file_name = 'movies.csv'
    list_of_id = []
    movies_details = {}

    def __init__(self,url,how_many_movies,output_file_name):
        self.url = url
        self.how_many_movies = how_many_movies
        self.output_file_name = output_file_name

    def id_spider(self):
        # This method will create a list of "n" movies id from IMDb

        page_text = requests.get(self.url).text
        soup = BeautifulSoup(page_text)
        movies = soup.findAll('td',{'class':'titleColumn'})

        for movie in movies:
            number = movie.text.split('.')[0]
            links = movie.findAll('a')
            for a in links:
                href = a.get('href')
                movie_id = self.parseing_spider(href)
            if int(number) <= self.how_many_movies:
                self.list_of_id.append(movie_id)

    def details_spider(self):
        # This spider will get a movies details by id from omdbapi and put them into dictionary {Title : Year}

        for movie_id in self.list_of_id:
            response = requests.get('http://www.omdbapi.com/?i='+movie_id)
            self.movies_details[response.json()['Title']] = response.json()['Year']

    def saving_spider(self):
        # This function will sort results and save to csv file
        with open(self.output_file_name, 'w') as f:
            w = csv.writer(f)
            w.writerows(sorted(self.movies_details.items(), key=lambda x: x[1]))

    @staticmethod
    def parseing_spider(href):
        # This little parser will get a movie id from a href

        movie_id = href.split('/')[2]
        return (movie_id)

# I dont know if it was a part of the test but I have noticed that We could get title and year directly from td

