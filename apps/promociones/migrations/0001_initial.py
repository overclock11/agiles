# Generated by Django 2.0.1 on 2018-01-29 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('identification', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
