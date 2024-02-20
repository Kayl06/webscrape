import requests
from bs4 import BeautifulSoup


class Scraper:
    def __init__(self, params):
        self.response = requests.get(params['url'])
        self.soup = BeautifulSoup(self.response.text, 'html.parser')

        self.title_tag = params['title_tag']
        self.title_attr = params['title_attr']
        self.author_tag = params['author_tag']
        self.author_attr = params['author_attr']
        self.date_tag = params['date_tag']
        self.datetime_attr = params['datetime_attr']
        self.date_attr = params['date_attr']
        self.content_tag = params['content_tag']
        self.content_attr = params['content_attr']

    def scrape_article(self):
        # Extract the article title
        title = self.soup.find(self.title_tag, self.title_attr).text.strip()

        # Extract the author name
        author = self.soup.find(self.author_tag, self.author_attr).text.strip()

        # Extract the published date
        published_date = self.soup.find(self.date_tag, self.datetime_attr)[
            self.date_attr].split('T')[0]

        # Extract the article content
        content = ''
        for paragraph in self.soup.find_all(self.content_tag, self.content_attr):
            content += paragraph.text.strip()

        return {
            'title': title,
            'author': author,
            'published_date': published_date,
            'content': content
        }
