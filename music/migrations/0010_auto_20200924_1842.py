# Generated by Django 3.1.1 on 2020-09-25 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0009_auto_20200924_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='added_by',
            field=models.CharField(default='admin', max_length=150),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
