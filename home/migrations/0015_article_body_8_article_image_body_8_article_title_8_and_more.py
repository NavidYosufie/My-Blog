# Generated by Django 4.0.6 on 2022-09-08 20:08

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_alter_article_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body_8',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='image_body_8',
            field=models.ImageField(blank=True, null=True, upload_to='article/imag'),
        ),
        migrations.AddField(
            model_name='article',
            name='title_8',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2022, 9, 8, 20, 8, 22, 611727, tzinfo=utc)),
        ),
    ]
