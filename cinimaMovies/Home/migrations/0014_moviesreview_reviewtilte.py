# Generated by Django 3.0.7 on 2020-08-16 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0013_moviesreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviesreview',
            name='reviewTilte',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
