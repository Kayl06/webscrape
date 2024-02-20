import sys
sys.path.append('/src/classes')

from src.classes.FileWriter import FileWriter
from src.classes.Scraper import Scraper


scraper_params_arr = [
    {
        'url': 'https://www.newyorker.com/news/annals-of-communications/the-stunning-end-of-dominions-case-against-fox-news',
        'title_tag': 'h1',
        'title_attr': {'data-testid': 'ContentHeaderHed'},
        'author_tag': 'a',
        'author_attr': {'class': 'byline__name-link'},
        'date_tag': 'time',
        'datetime_attr': {'data-testid': 'ContentHeaderPublishDate'},
        'date_attr': 'datetime',
        'content_tag': 'main',
        'content_attr': {'id': 'main-content'},
    },
    {
        'url': 'https://www.bbc.com/news/world-asia-65307858',
        'title_tag': 'h1',
        'title_attr': {'id': 'main-heading'},
        'author_tag': 'div',
        'author_attr': {'class': 'ssrcss-68pt20-Text-TextContributorName'},
        'date_tag': 'time',
        'datetime_attr': {'data-testid': 'timestamp'},
        'date_attr': 'datetime',
        'content_tag': 'main',
        'content_attr': {'id': 'main-content'},
    },
    {
        'url': 'https://www.nbcnews.com/news/world/sudan-conflict-warring-generals-western-interests-rcna80157',
        'title_tag': 'h1',
        'title_attr': {'class': 'article-hero-headline__htag'},
        'author_tag': 'span',
        'author_attr': {'class': 'byline-name'},
        'date_tag': 'time',
        'datetime_attr': {'class': 'relative'},
        'date_attr': 'datetime',
        'content_tag': 'div',
        'content_attr': {'class': 'article-body'},
    }

]

for idx, scraper in enumerate(scraper_params_arr):
    writer = FileWriter()
    scraper = Scraper(scraper)
    article_data = scraper.scrape_article()
    idx += 1

    print('\n================ Article #' + str(idx) +
          ': ' + article_data['title'] + ' ================')
    print('\n')
    print('Title:', article_data['title'])
    print('Author:', article_data['author'])
    print('Published Date:', article_data['published_date'])
    print('Content:', article_data['content'])
    print('\n================ End of Article #' +
          str(idx) + ' ================')
    print('\n')

    content = "\n"
    content += "\n================ Article #" + str(idx) + " ================"
    content += "Title:" + article_data['title']
    content += "\nAuthor:" + article_data['author']
    content += "\Published Date:" + article_data['published_date']
    content += "\Content:" + article_data['content']
    content += "\n================ End of Article #" + \
        str(idx) + " ================"
    content += "\n"

    writer.write(content)


print('success');