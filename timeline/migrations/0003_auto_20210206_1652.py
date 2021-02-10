# Generated by Django 3.1.3 on 2021-02-06 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeline', '0002_auto_20210206_1649'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panel',
            name='user',
        ),
        migrations.CreateModel(
            name='Timestamp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(max_length=255)),
                ('color', models.CharField(max_length=255)),
                ('panel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='timeline.panel')),
            ],
        ),
    ]
