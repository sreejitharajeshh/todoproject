# Generated by Django 5.0.1 on 2024-01-11 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2002-02-25'),
            preserve_default=False,
        ),
    ]
