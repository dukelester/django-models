# Generated by Django 3.2.4 on 2021-06-20 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0005_auto_20210619_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateField()),
                ('invited_reason', models.CharField(max_length=120)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.group')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models.person')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='models.Membership', to='models.Person'),
        ),
    ]
