import unittest
from app.models import NewsArticle
class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsArticle class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = NewsArticle('Scotlands papers','Kevin Richer','Pupil low test uptake and royal gran gesture','The front pages cover the birth of Meghan and Harry is baby and reports that pupils are not taking regular Covid tests.','https://www.bbc.co.uk/news/uk-scotland-57381085','skotlands.com/7643t94.jpg','2021-06-07T06:13:47Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,NewsArticle))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'Scotlands papers')
        self.assertEquals(self.new_article.author,'Kevin Richer')
        self.assertEquals(self.new_article.title,'Pupil low test uptake and royal gran gesture')
        self.assertEquals(self.new_article.description,'The front pages cover the birth of Meghan and Harry is baby and reports that pupils are not taking regular Covid tests.')
        self.assertEquals(self.new_article.url,'https://www.bbc.co.uk/news/uk-scotland-57381085')
        self.assertEquals(self.new_article.image,'skotlands.com/7643t94.jpg')
        self.assertEquals(self.new_article.date,'2021-06-07T06:13:47Z')