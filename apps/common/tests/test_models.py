from django.conf import settings
from django.test import TestCase
from apps.common import models
import os


class TestAboutModel(TestCase):
    test_img = "test_data/images/img.jpeg"

    def setUp(self):
        models.About.objects.create(
            image=self.test_img, title="test title", content="test content"
        )

    @property
    def get_single_model(self):
        return models.About.objects.first()

    def test_model_name(self):
        model = self.get_single_model

        self.assertEqual(str(model), model.__str__())

    def test_model_fields(self):
        model = self.get_single_model

        expected_url = os.path.join(settings.MEDIA_URL, self.test_img)

        self.assertEqual(model.title, "test title")
        self.assertEqual(model.content, "test content")
        self.assertEqual(model.image.url, expected_url)

    def test_without_data(self):
        models.About.objects.all().delete()

        model = self.get_single_model

        self.assertIsNone(model)