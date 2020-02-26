from django.db import models


class Languages(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"Name: {self.name}. Id: {self.pk}"


class CustomUser(models.Model):
    GENDER_CHOICES = (
        ("M", "Male"),
        ("F", "Female"),
    )

    PROFESSIONAL_CHOICES = (
        ("Y", "Yes"),
        ("N", "No"),
    )

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    card_number = models.CharField(blank=True, null=True, max_length=15)
    expire_date = models.DateField(blank=True, null=True)
    languages = models.ManyToManyField(Languages, through='LeadLanguages')
    professional = models.CharField(max_length=1, choices=PROFESSIONAL_CHOICES)

    def __str__(self):
        return f"name: {self.name}. id:{self.pk}"


class LeadLanguages(models.Model):
    lead = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
