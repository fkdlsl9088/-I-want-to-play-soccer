# Generated by Django 2.2.5 on 2020-08-11 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200811_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='check_in',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='check_out',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
