"""Test django models from app_users"""
from django.test import TestCase
from app_users import models


class ModelsTest(TestCase):
    """Test class model"""
    fixtures = ["data.json", "languages.json"]

    def test_str_lang(self):
        """Test method str from model language"""
        obj = models.Languages.objects.first()
        text = "Name: Ukraine. Id: 1"
        self.assertEqual(text, obj.__str__())

    def test_str_user(self):
        """Test method str from model user"""
        obj = models.CustomUser.objects.first()
        text = "name: test. id:1"
        self.assertEqual(text, obj.__str__())
