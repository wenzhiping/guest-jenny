# Generated by Django 2.2.1 on 2019-06-04 11:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0004_auto_20190604_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='guest',
            name='create_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
