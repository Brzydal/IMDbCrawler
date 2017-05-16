from IMDbCrawler import *
import os.path


class TestSpider:
    BlackWidow = Spider('http://www.imdb.com/chart/top?ref=ft_250', 100, 'movies.csv')

    def test_set_up(self):
        """
        Lets create our spider
        """

        self.BlackWidow = Spider('http://www.imdb.com/chart/top?ref=ft_250', 100, 'movies.csv')
        self.BlackWidow.id_spider()

    def test_parsing_spider(self):
        """
        First lets test if parser is working fine
        """

        movie_id = self.BlackWidow.parsing_spider(
            "/title/tt0068646/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2398042102&pf_rd_r=" +
            "05HJ9PZ18AMRNFAJKAR0&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_2")
        assert movie_id == 'tt0068646'

    def test_id_spider1(self):
        """
        Lets test if we will get 100 movies
        """

        assert len(self.BlackWidow.list_of_id) == 100

    def test_id_spider2(self):
        """
        Then test if id of first movie is ok (the test will fail if ranking in IMDb will change)
        """

        assert self.BlackWidow.list_of_id[0] == 'tt0111161'

    def test_id_spider3(self):
        """
        Then test if id of last movie is ok (the test will fail if ranking in IMDb will change)
        """

        assert self.BlackWidow.list_of_id[99] == 'tt0071853'

    def test_details_spider1(self):
        """
        Then lets test if for id tt0068646 we will get Godfather with Year of 1972
        """

        self.BlackWidow.movies_details = {}
        self.BlackWidow.list_of_id = ['tt0068646']
        self.BlackWidow.details_spider()
        assert list(self.BlackWidow.movies_details.keys())[0] == 'The Godfather'
        assert list(self.BlackWidow.movies_details.values())[0] == '1972'

    def test_details_spider2(self):
        """
        Then lets test if for id tt0208092 we will get Snatch with Year of 2000
        """

        self.BlackWidow.movies_details = {}
        self.BlackWidow.list_of_id = ['tt0208092']
        self.BlackWidow.details_spider()
        assert list(self.BlackWidow.movies_details.keys())[0] == 'Snatch'
        assert list(self.BlackWidow.movies_details.values())[0] == '2000'

    def test_saving_spider1(self):
        """
        Then lets test if saving spider created a file
        """
        self.BlackWidow.saving_spider()
        assert os.path.exists('movies.csv')

    def test_saving_spider2(self):
        """
        Then lets test if for specific movie details saving spider will create file with three rows
        """

        self.BlackWidow.movies_details = {'Three': 3, 'One': 1, 'Two': 2}
        self.BlackWidow.saving_spider()
        with open(self.BlackWidow.output_file_name, 'r') as f:
            row_count = sum(1 for row in f)
        assert row_count == 3

    def test_saving_spider3(self):
        """
        And test if  saving spider will create file with 100 rows
        """

        self.BlackWidow.list_of_id = []
        self.BlackWidow.id_spider()
        self.BlackWidow.movies_details = {}
        self.BlackWidow.details_spider()
        self.BlackWidow.saving_spider()
        with open(self.BlackWidow.output_file_name, 'r') as f:
            row_count = sum(1 for row in f)
        assert row_count == 100
>>>>>>> spider
