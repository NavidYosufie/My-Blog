# Generated by Django 4.0.6 on 2022-09-08 20:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_article_body_8_article_image_body_8_article_title_8_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='body_2',
        ),
        migrations.RemoveField(
            model_name='article',
            name='image_body_2',
        ),
        migrations.RemoveField(
            model_name='article',
            name='title_2',
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2022, 9, 8, 20, 9, 47, 236631, tzinfo=utc)),
        ),
    ]
