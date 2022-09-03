# Generated by Django 4.0.6 on 2022-09-03 14:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_coment_views_coment_nomber_massage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='body_4',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title_1',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title_2',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title_3',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='title_4',
            field=models.CharField(default=22, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2022, 9, 3, 14, 11, 45, 76411, tzinfo=utc)),
        ),
    ]