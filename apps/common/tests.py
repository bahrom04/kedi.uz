from django.test import TestCase
from apps.common import models


class TestAbout(TestCase):
    test_img = "test_data/images/img.jpeg"

    def test_about_data(self):
        models.About.objects.create(
            image=self.test_img, title="test title", content="test content"
        )
        about = models.About.objects.all()[0]
        
        self.assertEqual(about.title, "test title")
        self.assertEqual(about.content, "test content")


