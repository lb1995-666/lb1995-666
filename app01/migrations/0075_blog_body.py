# Generated by Django 3.2.7 on 2021-11-08 07:44

import DjangoUeditor.DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0074_auto_20211108_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body',
            field=DjangoUeditor.DjangoUeditor.models.UEditorField(blank=True, verbose_name='富文本内容'),
        ),
    ]
