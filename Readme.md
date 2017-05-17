# IMDb Crawler
Tiny bitsy spider to get year of production of 100 most popular movies and save it in a file. Project created as a part of an Interview for one of Warsaw companies.

## Task

1. Get data about top 100 movies from http://www.imdb.com/chart/top?ref=ft_250.  Check each movie link and scrape movie's ID that is a part or URL, for  instance: <a  href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=...  </a> The ID of this movie is "tt0111161"   


2. Having a list of 100 movie IDs get each movie details from http://www.omdbapi.com/?i=tt0111161


3. Having details of those 100 movies put movies into CSV file  sorted by year of production CSV will consists of only two columns:  title, year.


4. 100% test coverage is required (please use py.test)

## Solution
>I have created class Spider with a couple of attributes and methods which allow user to get id of how many movies he wants (from range 0-250, otherwise user have to change url by himself), later on  
user can get details of ths movies and save it in a csv file. For more details plese see following attributes and methods:

1. Attributes:
    * url - in our case it is a 'http://www.imdb.com/chart/top?ref=ft_250', if user want to get details of more movies or different movies he have to change it,
    * how_many_movies - 100 In our case it is 100 but it can be any number from range between 0 and 250 otherwise user have to change url,
    * output_file_name - custom file name, when file with this name already exists it will be overwritten. Because csv module was used to create a file it will be csv type,
    * list_of_id - a list in which id of movies will be stored,
    * movies_details  - a dictionary where details of movies will be stored, where key is the title and value is a year of production.

2. Methods:
    * id_spider - this method will create a list of "how many movies" movies id from IMDb
    * details_spider - this method will get a movies details by id from omdbapi and put them into dictionary called movies_details {Title : Year}
    * saving_spider - this method will sort details from a dictionary using unnamed lambda functiona and save them to csv file
    * parsing_spider(href) - this method get a href parameter and parse a movie id from a it.

3. BlackWidow:
