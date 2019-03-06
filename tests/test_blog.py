
import unittest
from app.models import Blog, User


class BlogTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Blog class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_blog= Blog(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_blog,Blog))


    def test_save_Blog(self):
       
        self.new_Blog.save_Blog() # saving the new Credentials
        self.assertTrue(len(Blog.query.all()>0)

    def test_get_blog_by_id(self):

        self.new_Blog.save_Blog()
        got_blogs = Blog.get_blog
