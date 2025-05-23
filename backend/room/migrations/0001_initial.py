# Generated by Django 3.2.11 on 2025-03-01 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('roomId', models.AutoField(primary_key=True, serialize=False)),
                ('number', models.CharField(max_length=255)),
                ('name', models.CharField(default='', max_length=30)),
                ('imgUrl', models.CharField(default='', max_length=300)),
                ('floor', models.CharField(default='1', max_length=30)),
                ('price', models.IntegerField(default=0)),
                ('area', models.CharField(default='0', max_length=30)),
            ],
        ),
    ]
