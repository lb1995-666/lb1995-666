# Generated by Django 3.2.7 on 2021-12-02 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0084_expert'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expert',
            options={'verbose_name': '达人管理', 'verbose_name_plural': '达人管理'},
        ),
        migrations.AddField(
            model_name='expert',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 2, 15, 35, 10, 443586), verbose_name='创建时间'),
        ),
    ]
