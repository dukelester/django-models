# Generated by Django 3.2.4 on 2021-06-19 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Musician',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('instruments', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('release_date', models.DateTimeField(verbose_name='date released')),
                ('number_stars', models.IntegerField(default=0)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.musician')),
            ],
        ),
    ]
