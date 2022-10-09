# Generated by Django 2.2.16 on 2022-10-09 17:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20220720_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='year',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(2022), django.core.validators.MinValueValidator(0)], verbose_name='Год создания'),
        ),
    ]
