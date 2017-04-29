from IMDbCrawler import *

# Lets create our spider
BlackWidow = Spider('http://www.imdb.com/chart/top?ref=ft_250',100,'movies.csv')

# First lets test if parser is working fine
def test_parsing_spider():
    movie_id = BlackWidow.parseing_spider("/title/tt0068646/?pf_rd_m=A2FGELUUNOQJNL&pf_rd_p=2398042102&pf_rd_r=05HJ9PZ18AMRNFAJKAR0&pf_rd_s=center-1&pf_rd_t=15506&pf_rd_i=top&ref_=chttp_tt_2")
    assert movie_id == 'tt0068646'

# Lets create a list of 100 movie id
BlackWidow.id_spider()

# Lets test if we will get 100 movies
def test_id_spider1():
    assert len(BlackWidow.list_of_id) == 100

# Then test if id of first movie is ok
def test_id_spider2():
    assert BlackWidow.list_of_id[0] == 'tt0111161'

# Then test if id of last movie is ok
def test_id_spider3():
    assert BlackWidow.list_of_id[99] == 'tt3783958'


# Then lets test if for id tt0068646 we will get Godfather with Year of 1972
def test_details_spider1():
    BlackWidow.movies_details = {}
    BlackWidow.list_of_id = ['tt0068646']
    BlackWidow.details_spider()
    assert BlackWidow.movies_details.keys()[0] == 'The Godfather'
    assert BlackWidow.movies_details.values()[0] == '1972'

# Then lets test if for id tt0208092 we will get Snatch with Year of 2000
def test_details_spider2():
    BlackWidow.movies_details = {}
    BlackWidow.list_of_id = ['tt0208092']
    BlackWidow.details_spider()
    assert BlackWidow.movies_details.keys()[0] == 'Snatch'
    assert BlackWidow.movies_details.values()[0] == '2000'