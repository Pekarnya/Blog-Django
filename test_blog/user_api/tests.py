from django.test import TestCase
from .models import News

# Create your tests here.


class NewsTestCase(TestCase):
    """
    NewsTestCase Checks content of the model instances

    Args:
        TestCase (django.test object): builtin class
    """

    @classmethod
    def setUpTestData(cls) -> None:
        News.objects.create(theme='TestTheme', body='Lorem Ipsum',
                            media_img='', media_video='')

    def test_theme_content(self):
        news = News.objects.get(id=1)
        expected_object_name = f'{news.theme}'
        self.assertEqual(expected_object_name, 'TestTheme')

    def test_body_content(self):
        news = News.objects.get(id=1)
        expected_object_name = f'{news.body}'
        self.assertEqual(expected_object_name, 'Lorem Ipsum')

    def test_img_content(self):
        news = News.objects.get(id=1)
        expected_object_name = f'{news.media_img}'
        self.assertEqual(expected_object_name, '')

    def test_media_content(self):
        news = News.objects.get(id=1)
        expected_object_name = f'{news.media_video}'
        self.assertEqual(expected_object_name, '')
