# Generated by Django 3.2.11 on 2025-03-01 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
