import requests as rq
from bs4 import BeautifulSoup


def get_posts(soup):
    return soup.select('body main.page-content div.wrapper div.home div.p')

def data_parse(posts):
    for post in posts:
        title = post.find('h3').text.strip()
        descript = post.find('h4').text.strip()
        author = post.find('h5').text.strip()
        print(title, descript, author)