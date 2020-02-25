from django.test import TestCase
from app_users import models


class FormsTest(TestCase):
    fixtures = ["data.json", "languages.json"]

    def test_str_lang(self):
        obj = models.Languages.objects.first()
        text = "Name: Ukraine. Id: 1"
        self.assertEqual(text, obj.__str__())

    def test_str_user(self):
        obj = models.CustomUser.objects.first()
        text = "name: test. id:1"
        self.assertEqual(text, obj.__str__())
