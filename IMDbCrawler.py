import requests
from bs4 import BeautifulSoup
import csv


class Spider:

    """
    A Spider which will gather information about 'n' movies from website (IMDb) and save it in a file
    """

    url = 'http://www.imdb.com/chart/top?ref=ft_250'
    how_many_movies_ = 100  # In our case min 0 max 250 otherwise we have to change url
    output_file_name = 'movies.csv'
    list_of_id = []
    movies_details = {}

    def __init__(self, url, how_many_movies, output_file_name):
        self.url = url
        self.how_many_movies = how_many_movies
        self.output_file_name = output_file_name

    def id_spider(self):

        """
        This method will create a list of "n" movies id from IMDb
        """

        movie_id = None
        page_text = requests.get(self.url).text
        soup = BeautifulSoup(page_text, "lxml")
        movies = soup.findAll('td', {'class': 'titleColumn'})
        for movie in movies:
            number = movie.text.split('.')[0]
            links = movie.findAll('a')
            for a in links:
                href = a.get('href')
                movie_id = self.parsing_spider(href)
            if int(number) <= self.how_many_movies:
                self.list_of_id.append(movie_id)

    def details_spider(self):

        """
        This spider will get a movies details by id from omdbapi and put them into dictionary {Title : Year}
        """

        for movie_id in self.list_of_id:
            response = requests.get('http://www.omdbapi.com/?i=' + movie_id)
            self.movies_details[response.json()['Title']] = response.json()['Year']

    def saving_spider(self):

        """
        This function will sort results and save to csv file
        :return a file with 100 movies
        """

        with open(self.output_file_name, 'w') as f:
            w = csv.writer(f)
            w.writerows(sorted(self.movies_details.items(), key=lambda x: x[1]))  # Sort by year, ascending

    @staticmethod
    def parsing_spider(href):
        #
        """
        This little parser will get a movie id from a href
        :param href:
        :return: movie_id
        """
        movie_id = href.split('/')[2]
        return movie_id

if __name__ == "__main__":
    print("### Starting Spider! ###")
    BlackWidow = Spider('http://www.imdb.com/chart/top?ref=ft_250', 100, 'movies.csv')
    BlackWidow.id_spider()
    print(len(BlackWidow.list_of_id))
    BlackWidow.details_spider()
    print(BlackWidow.movies_details)
    BlackWidow.saving_spider()
    print("### Spider has left... ###")

