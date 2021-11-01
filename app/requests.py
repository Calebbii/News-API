import urllib.request,json
from .models import NewsSource,NewsArticle

# Getting the api_key
api_key = None
# Getting the news base url
base_url = None
#Getting the article url
article_url = None

def confige_request(app):
    global api_key,base_url,article_url
    api_key = app.config['NEWS_API_KEY']
    base_url = app.config['NEWS_API_SOURCE_URL']
    article_url = app.config['NEWS_API_ARTICLE_URL']

def get_NewsSource(category):

    get_NewsSources_URL = base_url.format(category,api_key)
    

    with urllib.request.urlopen(get_NewsSources_URL) as url:
        get_NewsSource_data = url.read()
        get_NewsSource_response = json.loads(get_NewsSource_data)

        get_NewsSource_results = None 

        if get_NewsSource_response['sources']:
            get_NewsSource_results_list = get_NewsSource_response['sources']
            get_NewsSource_results = process_NewsSource(get_NewsSource_results_list)

    return get_NewsSource_results        

def process_NewsSource(news_list):
    NewsSource_results = []
    for NewsSource_item in news_list:
        id = NewsSource_item.get('id')
        name = NewsSource_item.get('name')
        description = NewsSource_item.get('description')
        url = NewsSource_item.get('url')
        category = NewsSource_item.get('category')
        language = NewsSource_item.get('language')
        country = NewsSource_item.get('country')

        NewsSource_object = NewsSource(id,name,description,url,language,category,country)

        NewsSource_results.append(NewsSource_object)

    return NewsSource_results
    
def get_articles(id):
    get_article_url = article_url.format(id,api_key)


    with urllib.request.urlopen(get_article_url) as url:
        article_data = url.read()
        article_response = json.loads(article_data)

        articles_results = None

        if article_response['articles']:
            articles_results_list = article_response['articles']
            articles_results = process_articles(articles_results_list)
            

    return articles_results



def process_articles(articles_list):

    articles_results = []
    for news_article_item in articles_list:
        id = news_article_item.get('id')
        author = news_article_item.get('author')
        title = news_article_item.get('title')
        description = news_article_item.get('description')
        url = news_article_item.get('url')
        image = news_article_item.get('urlToImage')
        date = news_article_item.get('publishedAt')

        article_object = NewsArticle(id,author,title,description,url,image,date)

        articles_results.append(article_object)


    return articles_results