# Generated by Django 2.2.1 on 2019-06-04 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sign', '0003_auto_20190604_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='guest',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
