from django.test import TestCase
from .models import Blog

# Create your tests here.
class BlogTestCase(TestCase):
    def test_save_without_content(self):
        blog = Blog.objects.create(title="Test Blog")
        self.assertEqual(blog.content, None)
        self.assertEqual(Blog.objects.all().count(), 1)

    def test_save_with_content(self):
        with self.assertRaises(RecursionError):
            blog = Blog.objects.create(title="title", content="This is a test blog")
