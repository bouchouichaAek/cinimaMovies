# Generated by Django 3.0.7 on 2020-08-12 13:16

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0003_movies_reviewmovie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='reviewMovie',
        ),
        migrations.AddField(
            model_name='movies',
            name='reviewMovie',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
