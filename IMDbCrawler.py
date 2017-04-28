import requests

def spider(url):
    html = requests.get(url).text
    for link in html.findAll('a',{'class':'titleColumn'}):
        href = link.get('href')
        print(href)



spider('http://www.imdb.com/chart/top?ref=ft_250')