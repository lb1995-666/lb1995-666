# Generated by Django 3.2.7 on 2021-12-13 08:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0087_auto_20211213_1131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='leavemessage',
            options={'verbose_name': '用户留言内容', 'verbose_name_plural': '用户留言内容'},
        ),
        migrations.AddField(
            model_name='leavemessage',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 16, 22, 29, 465913), verbose_name='创建时间'),
        ),
        migrations.AddField(
            model_name='leavemessage',
            name='leave_user',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.users', verbose_name='留言者'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 16, 22, 29, 465913), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 16, 22, 29, 465913), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='expert',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 16, 22, 29, 466910), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='shops',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 13, 16, 22, 29, 462921), verbose_name='创建时间'),
        ),
    ]
