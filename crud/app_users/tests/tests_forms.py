from django.test import TestCase
from app_users import forms


class FormsTest(TestCase):
    fixtures = ["data.json", "languages.json"]

    def test_validate_card_number_is_none(self):
        data = {"name": "test2", "gender": "M", "professional": "N", "languages": [1]}
        form = forms.CustomUserCreate(data)
        self.assertEqual(form.is_valid(), True)

    def test_validate_card_number_not_none(self):
        data = {
            "name": "test2",
            "gender": "M",
            "card_number": "12345678",
            "expire_date": "2020-11-23",
            "professional": "N",
            "languages": [1],
        }
        form = forms.CustomUserCreate(data)
        self.assertEqual(form.is_valid(), True)

    def test_validate_card_number_symbol_true(self):
        data = {
            "name": "test2",
            "gender": "M",
            "card_number": "12W42T6X8",
            "expire_date": "2024-11-23",
            "professional": "N",
            "languages": [1],
        }
        form = forms.CustomUserCreate(data)
        self.assertEqual(form.is_valid(), True)

    def test_validate_card_number_symbol_false(self):
        data = {
            "name": "test2",
            "gender": "M",
            "card_number": "12W42TS6X8",
            "expire_date": "2024-10-10",
            "professional": "N",
            "languages": [1],
        }
        form = forms.CustomUserCreate(data)
        text_error = "* Input valid data in card"
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.errors.get("card_number").as_text(), text_error)

    def test_validate_card_number_symbol_lengs_false(self):
        data = {
            "name": "test2",
            "gender": "M",
            "card_number": "12543",
            "expire_date": "2024-11-23",
            "professional": "N",
            "languages": [1],
        }
        form = forms.CustomUserCreate(data)
        text_error = "* Length must been: 8-15 symbols "
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.errors.get("card_number").as_text(), text_error)

    def test_validate_card_number_symbol_lengs_True(self):
        data = {
            "name": "test2",
            "gender": "M",
            "card_number": "1234567890T234W",
            "expire_date": "2024-11-23",
            "professional": "N",
            "languages": [1],
        }
        form = forms.CustomUserCreate(data)
        self.assertEqual(form.is_valid(), True)

    def test_validate_expire_date_none_false(self):
        data = {
            "name": "test2",
            "gender": "M",
            "card_number": "125432352",
            "professional": "N",
            "languages": [1],
        }
        form = forms.CustomUserCreate(data)
        text_error = "* Input date card"
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.errors.get("expire_date").as_text(), text_error)

    def test_validate_expire_date_not_none_true(self):
        data = {
            "name": "test2",
            "gender": "M",
            "card_number": "125432352",
            "expire_date": "2024-11-23",
            "professional": "N",
            "languages": [1],
        }
        form = forms.CustomUserCreate(data)
        self.assertEqual(form.is_valid(), True)

    def test_validate_expire_date_date_less_false(self):
        data = {
            "name": "test2",
            "gender": "M",
            "card_number": "125432352",
            "expire_date": "2020-01-23",
            "professional": "N",
            "languages": [1],
        }
        form = forms.CustomUserCreate(data)
        text_error = "* Not valid date card"
        self.assertEqual(form.is_valid(), False)
        self.assertEqual(form.errors.get("expire_date").as_text(), text_error)
