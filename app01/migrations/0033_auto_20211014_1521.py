# Generated by Django 3.2.7 on 2021-10-14 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0032_auto_20211014_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shops',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterField(
            model_name='shops',
            name='commodity_price',
            field=models.FloatField(blank=True, max_length=255, verbose_name='商品价格'),
        ),
    ]
