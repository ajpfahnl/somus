# Generated by Django 3.1.1 on 2020-09-25 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_auto_20200922_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='playlist',
            name='added_by',
            field=models.CharField(default='admin', max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='added_by',
            field=models.CharField(default='admin', max_length=150),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=150),
        ),
    ]
