# Generated by Django 3.2.7 on 2021-11-03 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0070_book_book_name2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_name2',
        ),
    ]
