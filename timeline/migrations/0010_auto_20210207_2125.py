# Generated by Django 3.1.3 on 2021-02-07 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0009_auto_20210207_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='description',
            field=models.CharField(max_length=255),
        ),
    ]