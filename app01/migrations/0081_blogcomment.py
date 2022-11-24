# Generated by Django 3.2.7 on 2021-11-11 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0080_alter_blog_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_context', models.CharField(max_length=255, verbose_name='评论内容')),
                ('create_time', models.CharField(max_length=255, verbose_name='创建时间')),
                ('blog_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.blog')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app01.users')),
            ],
        ),
    ]
