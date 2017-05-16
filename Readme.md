# IMDb Crawler
Tiny bitsy spider to get year of production of 100 most popular movies and save it in a file. Project created as a part of an Interview for one of Warsaw companies.

## the Task

1. Get data about top 100 movies from http://www.imdb.com/chart/top?ref=ft_250.  Check each movie link and scrape movie's ID that is a part or URL, for  instance: <a  href="/title/tt0111161/?pf_rd_m=A2FGELUUNOQJNL&amp;pf_rd_p=...  </a> The ID of this movie is "tt0111161"   


2. Having a list of 100 movie IDs get each movie details from http://www.omdbapi.com/?i=tt0111161


3. Having details of those 100 movies put movies into CSV file  sorted by year of production CSV will consists of only two columns:  title, year.


4. 100% test coverage is required (please use py.test)
