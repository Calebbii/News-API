
import unittest
from app.models import NewsSource

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the NewsSource class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = NewsSource('new-scientist','New Scientist','Breaking science and technology news from around the world.','https://www.newscientist.com/section/news','science','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,NewsSource))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_source.id,'new-scientist')
        self.assertEquals(self.new_source.name,'New Scientist')
        self.assertEquals(self.new_source.description,'Breaking science and technology news from around the world.')
        self.assertEquals(self.new_source.url,'https://www.newscientist.com/section/news')
        self.assertEquals(self.new_source.category,'science')
        self.assertEquals(self.new_source.country,'us')