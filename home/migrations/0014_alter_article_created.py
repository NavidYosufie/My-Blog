# Generated by Django 4.0.6 on 2022-09-08 19:49

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_article_body_5_article_body_6_article_body_7_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2022, 9, 8, 19, 49, 12, 289160, tzinfo=utc)),
        ),
    ]
