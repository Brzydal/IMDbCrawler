from IMDbCrawler import *

Black_Widow = spiders_mum('http://www.imdb.com/chart/top?ref=ft_250', 100, 'movies.csv')


def test_id_spider1():
    """
    First lets test if we will get 100 movies
    """

    assert len(id_spider('http://www.imdb.com/chart/top?ref=ft_250', 100)) == 100


def test_id_spider2():
    """
    Then test if id of first movie is ok
    """
    assert id_spider('http://www.imdb.com/chart/top?ref=ft_250', 100)[0] == 'tt0111161'


def test_id_spider3():
    """
    Then test if id of last movie is ok
    """
    assert id_spider('http://www.imdb.com/chart/top?ref=ft_250', 100)[99] == 'tt3783958'


def test_details_spider1():
    """
    Then lets test if for id tt0068646 we will get Godfather with Year of 1972
    """
    assert details_spider(['tt0068646']).keys()[0] == 'The Godfather'
    assert details_spider(['tt0068646']).values()[0] == '1972'


def test_details_spider2():
    """
    Then lets test if for id tt0208092 we will get Snatch with Year of 2000
    """
    assert details_spider(['tt0208092']).keys()[0] == 'Snatch'
    assert details_spider(['tt0208092']).values()[0] == '2000'
