# Generated by Django 2.0.7 on 2018-07-24 13:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 24, 13, 22, 52, 745821), verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='modified_time',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 24, 13, 22, 52, 745821), verbose_name='最后一次修改'),
        ),
    ]
