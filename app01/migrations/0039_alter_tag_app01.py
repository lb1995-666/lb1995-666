# Generated by Django 3.2.7 on 2021-10-14 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0038_auto_20211014_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='app01',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.app01s'),
        ),
    ]
