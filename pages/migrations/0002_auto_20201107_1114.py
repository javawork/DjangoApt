# Generated by Django 3.1.2 on 2020-11-07 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aptrent',
            name='date',
            field=models.CharField(max_length=24),
        ),
        migrations.AlterField(
            model_name='apttrade',
            name='date',
            field=models.CharField(max_length=24),
        ),
    ]
