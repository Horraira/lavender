# Generated by Django 4.0 on 2021-12-26 02:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0007_alter_mobile_jancode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='janCode',
            field=models.DecimalField(decimal_places=0, max_digits=13, unique=True, validators=[django.core.validators.MinValueValidator(8)]),
        ),
    ]
