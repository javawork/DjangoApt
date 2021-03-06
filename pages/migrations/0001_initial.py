# Generated by Django 3.1.2 on 2020-11-07 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AptRent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('deposit', models.IntegerField()),
                ('rent_price', models.IntegerField()),
                ('size', models.FloatField()),
                ('dong', models.CharField(max_length=12)),
                ('built_year', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('date', models.DateField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AptTrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('price', models.IntegerField()),
                ('size', models.FloatField()),
                ('dong', models.CharField(max_length=12)),
                ('built_year', models.IntegerField()),
                ('floor', models.IntegerField()),
                ('date', models.DateField()),
                ('cdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
