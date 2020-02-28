""" Test djan g"""
from django.test import TestCase
from app_users import models
from app_users.views import FormSetMixin


class ViewsTest(TestCase):
    """Testing """
    fixtures = ["data.json"]

    def test_delete_one_user_true(self):
        """test delete one user. Status = True"""
        objects = models.CustomUser.objects.count()
        response = self.client.post("/leads/delete", {"1": "True"})
        self.assertLess(models.CustomUser.objects.count(), objects)
        self.assertEqual(response.status_code, 302)

    def test_delete_one_user_false(self):
        """test delete one user. Status = False"""
        objects = models.CustomUser.objects.count()
        response = self.client.post("/leads/delete", {"14": "True"})
        self.assertEqual(models.CustomUser.objects.count(), objects)
        self.assertEqual(response.status_code, 302)

    def test_delete_more_users_true(self):
        """test delete 2 users. Status = True"""
        objects = models.CustomUser.objects.count()
        response = self.client.post("/leads/delete", {"1": "True", "2": "True"})
        self.assertEqual(models.CustomUser.objects.count(), objects - 2)
        self.assertEqual(response.status_code, 302)

    def test_delete_more_users_false(self):
        """test delete 2 users. Status = False"""
        objects = models.CustomUser.objects.count()
        response = self.client.post("/leads/delete", {"15": "True",
                                                      "221": "True"})
        self.assertEqual(models.CustomUser.objects.count(), objects)
        self.assertEqual(response.status_code, 302)

    def test_formset_mixin_create_object(self):
        """Create object with none field"""
        objects = models.CustomUser.objects.count()
        data = {
            'name': ['NEW'], 'gender': ['M'],
            'leadlanguages_set-TOTAL_FORMS': ['1'],
            'leadlanguages_set-INITIAL_FORMS': ['0'],
            'leadlanguages_set-MIN_NUM_FORMS': ['0'],
            'leadlanguages_set-MAX_NUM_FORMS': ['1000'],
            'leadlanguages_set-0-lead': [''],
            'leadlanguages_set-0-language': [''],
            'leadlanguages_set-0-id': [''], 'card_number': [''],
            'expire_date': [''], 'professional': ['Y']
        }
        response = self.client.post("/leads/create/", data=data)
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(models.CustomUser.objects.count(), objects)

    def test_create_more_langs(self):
        """Test create 3 language to one user. Status = True"""
        objects = models.CustomUser.objects.count()
        data = {
            'name': ['test'], 'gender': ['M'],
            'leadlanguages_set-TOTAL_FORMS': ['4'],
            'leadlanguages_set-INITIAL_FORMS': ['0'],
            'leadlanguages_set-MIN_NUM_FORMS': ['0'],
            'leadlanguages_set-MAX_NUM_FORMS': ['1000'],
            'leadlanguages_set-0-lead': [''], 'leadlanguages_set-0-id': [''],
            'leadlanguages_set-1-lead': [''],
            'leadlanguages_set-1-language': ['1'],
            'leadlanguages_set-1-id': [''], 'leadlanguages_set-2-lead': [''],
            'leadlanguages_set-2-language': ['2'],
            'leadlanguages_set-2-id': [''], 'leadlanguages_set-3-lead': [''],
            'leadlanguages_set-3-language': ['3'],
            'leadlanguages_set-3-id': [''], 'card_number': [''],
            'expire_date': [''], 'professional': ['Y']
        }
        response = self.client.post("/leads/create/", data=data)
        self.assertEqual(response.status_code, 302)
        self.assertNotEqual(models.CustomUser.objects.count(), objects)
