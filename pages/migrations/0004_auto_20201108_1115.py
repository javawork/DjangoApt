# Generated by Django 3.1.2 on 2020-11-08 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20201107_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='aptrent',
            name='month',
            field=models.CharField(blank=True, default='', max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='apttrade',
            name='month',
            field=models.CharField(blank=True, default='', max_length=8, null=True),
        ),
    ]
