# Generated by Django 3.2.4 on 2021-06-20 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0008_ox'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('age', models.PositiveIntegerField()),
                ('home_group', models.CharField(max_length=45)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
