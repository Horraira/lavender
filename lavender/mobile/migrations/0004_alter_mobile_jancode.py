# Generated by Django 4.0 on 2021-12-25 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobile', '0003_rename_mobilename_mobile_modelname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobile',
            name='janCode',
            field=models.IntegerField(unique=True),
        ),
    ]
