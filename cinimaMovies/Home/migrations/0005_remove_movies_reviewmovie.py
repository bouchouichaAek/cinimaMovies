# Generated by Django 3.0.7 on 2020-08-14 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_auto_20200812_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='reviewMovie',
        ),
    ]
