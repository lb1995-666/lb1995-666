# Generated by Django 3.2.7 on 2021-11-08 06:56

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0073_alter_blog_context'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.CharField(default=0, max_length=255, verbose_name='阅读量'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='context',
            field=tinymce.models.HTMLField(blank=True, verbose_name='内容'),
        ),
    ]
