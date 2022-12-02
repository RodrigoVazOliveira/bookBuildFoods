# Generated by Django 4.1.3 on 2022-11-30 11:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0003_recipe_people_alter_recipe_date_time_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='published',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='date_time_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 11, 30, 8, 41, 16, 161214)),
        ),
    ]