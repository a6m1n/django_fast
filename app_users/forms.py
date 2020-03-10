"""My custom Django forms"""
import datetime
from django import forms
from django.forms import ModelForm, inlineformset_factory
from app_users.models import CustomUser, LeadLanguages


class FormControlMixin:
    """From control mixin who add class form-control to all fields"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if field.label is not None:
                field.widget.attrs.update({"class": "form-control"})


class CustomUserCreate(FormControlMixin, ModelForm):
    """ ModelForm with mixin """
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
        """Clear calendar method. Delete with clean expire date"""
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

        if len(card_number) < 8:
            raise forms.ValidationError("Length must been: 8-15 symbols ")

        for digit in card_number:
            if digit not in accept_values:
                raise forms.ValidationError("Input valid data in card")

        return card_number

    def clean_expire_date(self):
        """Expire date clean method. Delete with clean card_number"""
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
    """LanguageUser form. Lead==user"""
    class Meta:
        model = LeadLanguages
        fields = ["lead", "language"]


LanguageFormset = inlineformset_factory(
    CustomUser, LeadLanguages, extra=1, form=LanguageFrom
)
