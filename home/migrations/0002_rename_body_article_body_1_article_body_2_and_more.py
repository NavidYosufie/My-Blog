# Generated by Django 4.0.6 on 2022-09-03 11:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='body',
            new_name='body_1',
        ),
        migrations.AddField(
            model_name='article',
            name='body_2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='body_3',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateField(default=datetime.datetime(2022, 9, 3, 11, 13, 50, 111825, tzinfo=utc)),
        ),
    ]
