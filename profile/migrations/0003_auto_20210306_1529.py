# Generated by Django 3.1.3 on 2021-03-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0002_auto_20210306_1528'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(),
        ),
    ]
