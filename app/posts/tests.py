from django.test import TestCase
from .models import Post


class PostTestCase(TestCase):

    def setUp(self):
        # post name
        self.blog = Post.objects.create(
            name="my name is Asadbek", body="Asadbek hi bro"
        )

    def test_post_model(self):
        d = self.blog
        self.assertTrue(isinstance(d, Post))
        self.assertEqual(str(d), "my name is Asadbek")
