# Generated by Django 3.2.11 on 2025-03-09 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0005_order_assigntime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='assignTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='finishTime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='submitTime',
            field=models.DateTimeField(),
        ),
    ]
