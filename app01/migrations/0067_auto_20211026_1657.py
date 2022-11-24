# Generated by Django 3.2.7 on 2021-10-26 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0066_overtimeorleave_approver_opinion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=255, verbose_name='角色名称')),
            ],
        ),
        migrations.AlterModelOptions(
            name='overtimeorleave',
            options={'verbose_name': '请假/调休申请', 'verbose_name_plural': '请假/调休申请'},
        ),
        migrations.AlterModelOptions(
            name='users',
            options={'verbose_name': '网站用户', 'verbose_name_plural': '网站用户'},
        ),
        migrations.AlterField(
            model_name='overtimeorleave',
            name='approver_opinion',
            field=models.TextField(blank=True, max_length=2048, verbose_name='审批意见'),
        ),
    ]
