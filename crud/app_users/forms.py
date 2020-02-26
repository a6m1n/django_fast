import datetime

from django import forms
from django.forms import ModelForm, modelformset_factory, \
    inlineformset_factory, BaseInlineFormSet

from .models import CustomUser, Languages, LeadLanguages


class FormControlMixin:
    """From control mixin who add class form-control to all fields"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            if field.label is not None:
                field.widget.attrs.update({"class": "form-control"})


class CustomUserCreate(FormControlMixin, ModelForm):
    gender = forms.ChoiceField(
        choices=CustomUser.GENDER_CHOICES, widget=forms.RadioSelect
    )

    professional = forms.ChoiceField(
        choices=CustomUser.PROFESSIONAL_CHOICES, widget=forms.RadioSelect
    )

    def __init__(self, *args, **kwargs):
        """added html attrs to class (added only to form!)"""
        super().__init__(*args, **kwargs)

    def clean_card_number(self):
        card_number = self.cleaned_data.get("card_number")
        accept_values = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            "X",
            "T",
            "W",
        ]
        if not card_number:
            return card_number

        if 8 > len(card_number):
            raise forms.ValidationError("Length must been: 8-15 symbols ")

        for digit in card_number:
            if digit not in accept_values:
                raise forms.ValidationError("Input valid data in card")

        return card_number

    # def clean_languages(self):
    #     languages = [Languages.objects.all()]
    #     # lang2 = [Languages.objects.filter(pk=1)]
    #     # self.cleaned_data['languages'] = languages
    #
    #     # print(self.instance.languages.set(*languages))
    #     return languages

    # def is_valid(self, *args, **kwargs):
    #     self.errors
    #     self.clean_languages()
    #
    #     # print(self.cleaned_data)
    #     # print(self.data)
    #     return super().is_valid(*args, **kwargs)

    def clean_expire_date(self):
        card_number = self.cleaned_data.get("card_number")
        if not card_number:
            return None

        expire_date = self.cleaned_data.get("expire_date")
        if not expire_date:
            raise forms.ValidationError("Input date card")

        current_date = datetime.datetime.now(datetime.timezone.utc).date()
        value = expire_date - current_date

        if datetime.timedelta(30 * 6) >= value:
            raise forms.ValidationError("Not valid date card")

        return expire_date

    class Meta:
        model = CustomUser
        fields = [
            "name",
            "gender",
            "card_number",
            "expire_date",
            "professional",
        ]


class LanguageFrom(FormControlMixin, ModelForm):
    class Meta:
        model = LeadLanguages
        fields = ["lead", 'language']


LanguageFormset = inlineformset_factory(
    CustomUser, LeadLanguages, extra=1, form=LanguageFrom
)
