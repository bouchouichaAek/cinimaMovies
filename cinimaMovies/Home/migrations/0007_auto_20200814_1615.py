# Generated by Django 3.0.7 on 2020-08-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_auto_20200814_1545'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActorsTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Actor', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Director', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='movies',
            old_name='movieName',
            new_name='movieTitle',
        ),
        migrations.AddField(
            model_name='movies',
            name='releaseDate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='movies',
            name='Actors',
            field=models.ManyToManyField(to='Home.ActorsTable'),
        ),
        migrations.AddField(
            model_name='movies',
            name='Director',
            field=models.ManyToManyField(to='Home.Director'),
        ),
    ]
