from django import forms
from django.forms import ModelForm

from .models import CustomUser


class FormControlMixin:
    """From control mixin who add class form-control to all fields"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if field.label is not None:
                field.widget.attrs.update({"class": "form-control"})


class CustomUserCreate(FormControlMixin, ModelForm):
    gender = forms.ChoiceField(choices=CustomUser.GENDER_CHOICES,
                               widget=forms.RadioSelect)

    professional = forms.ChoiceField(choices=CustomUser.PROFESSIONAL_CHOICES,
                                     widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        """added html attrs to class (added only to form!)"""
        super().__init__(*args, **kwargs)

    class Meta:
        model = CustomUser
        fields = [
            'name',
            'gender',
            'card_number',
            'expire_date',
            'languages',
            'professional'
        ]