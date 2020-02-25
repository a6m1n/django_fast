# Generated by Django 2.2.10 on 2020-02-24 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Languages",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
                ("card_number", models.PositiveIntegerField()),
                ("expire_date", models.DateField()),
                (
                    "professional",
                    models.CharField(choices=[("Y", "Yes"), ("N", "No")], max_length=1),
                ),
                ("languages", models.ManyToManyField(to="app_users.Languages")),
            ],
        ),
    ]
