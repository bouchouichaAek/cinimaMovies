# Generated by Django 3.0.7 on 2020-08-16 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Home', '0012_auto_20200814_1747'),
    ]

    operations = [
        migrations.CreateModel(
            name='MoviesReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Moviesreview', models.TextField()),
                ('Timestamp', models.DateTimeField(auto_now_add=True)),
                ('MoviesTilte', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.Movies')),
                ('ReviewAuthor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
