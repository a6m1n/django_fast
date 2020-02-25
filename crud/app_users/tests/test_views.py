from django.test import TestCase
from app_users import models


class ViewsTest(TestCase):
    fixtures = ["data.json"]

    def test_delete_one_user_true(self):
        objects = models.CustomUser.objects.count()
        response = self.client.post("/leads/delete", {"1": "True"})
        self.assertLess(models.CustomUser.objects.count(), objects)
        self.assertEqual(response.status_code, 302)

    def test_delete_one_user_false(self):
        objects = models.CustomUser.objects.count()
        response = self.client.post("/leads/delete", {"14": "True"})
        self.assertEqual(models.CustomUser.objects.count(), objects)
        self.assertEqual(response.status_code, 302)

    def test_delete_more_users_true(self):
        objects = models.CustomUser.objects.count()
        response = self.client.post("/leads/delete", {"1": "True", "2": "True"})
        self.assertEqual(models.CustomUser.objects.count(), objects - 2)
        self.assertEqual(response.status_code, 302)

    def test_delete_more_users_false(self):
        objects = models.CustomUser.objects.count()
        response = self.client.post("/leads/delete", {"15": "True", "221": "True"})
        self.assertEqual(models.CustomUser.objects.count(), objects)
        self.assertEqual(response.status_code, 302)
