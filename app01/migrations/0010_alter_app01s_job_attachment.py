# Generated by Django 3.2.7 on 2021-09-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_auto_20210923_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='app01s',
            name='job_attachment',
            field=models.FileField(blank=True, upload_to='attachment', verbose_name='其他附件'),
        ),
    ]
