# Generated by Django 4.0.6 on 2022-09-05 11:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_article_image_body_1_article_image_body_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2022, 9, 5, 11, 54, 28, 45066, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='article',
            name='image_body_4',
            field=models.ImageField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='article',
            name='tip',
            field=models.TextField(blank=True),
        ),
    ]
