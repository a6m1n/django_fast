# Generated by Django 2.2.10 on 2020-02-25 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_users", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="card_number",
            field=models.CharField(max_length=12),
        ),
    ]