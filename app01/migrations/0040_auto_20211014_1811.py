# Generated by Django 3.2.7 on 2021-10-14 10:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0039_alter_tag_app01'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shops',
            name='commodity_type',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app01.shoptypes', verbose_name='商品类型'),
        ),
        migrations.AlterField(
            model_name='shoptypes',
            name='shop_type_name',
            field=models.CharField(max_length=255, unique=True, verbose_name='商品类型名称'),
        ),
    ]
