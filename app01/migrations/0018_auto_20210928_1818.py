# Generated by Django 3.2.7 on 2021-09-28 10:18

import app01.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0017_app01s_even_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='app01s',
            name='create_date',
            field=models.DateField(default=None, verbose_name='创建日期'),
        ),
    ]
