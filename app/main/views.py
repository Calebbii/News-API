from flask import render_template,request,redirect,url_for
from ..requests import get_NewsSource,get_articles
from ..models import NewsArticle,NewsSource
from . import main

@main.route('/')
def index():
    business = get_NewsSource('business')
    entertainment = get_NewsSource('entertainment')
    health  = get_NewsSource('health')
    science = get_NewsSource('science')
    sports = get_NewsSource('sports')
    technology = get_NewsSource('technology')
    title = 'News Centre'

    return render_template('index.html',title = title, business = business,entertainment = entertainment,health = health,science = science, sports = sports,technology = technology)

@main.route('/newsarticles/<id>')
def article(id):
    article = get_articles(id)
    title = f'{id}'
    return render_template('newsarticles.html',title= title, articles = article)