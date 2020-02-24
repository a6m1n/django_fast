from django.db import models


class Languages(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Name: {self.name}. Id: {self.pk}'


class CustomUser(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    PROFESSIONAL_CHOICES = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )

    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    card_number = models.PositiveIntegerField()
    expire_date = models.DateField()
    languages = models.ManyToManyField(Languages)
    professional = models.CharField(max_length=1, choices=PROFESSIONAL_CHOICES)

    def __str__(self):
        return f'name: {self.name}. id:{self.pk}'
