# Generated by Django 3.2.7 on 2021-12-13 08:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0088_auto_20211213_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 16, 32, 33, 25414), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 16, 32, 33, 25414), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='expert',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 16, 32, 33, 26411), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='leavemessage',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 16, 32, 33, 26411), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='leavemessage',
            name='leave_user',
            field=models.CharField(default='', max_length=2000, verbose_name='留言用户'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 16, 32, 33, 22422), verbose_name='创建时间'),
        ),
    ]
