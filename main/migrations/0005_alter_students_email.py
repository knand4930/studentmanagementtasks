# Generated by Django 3.2.9 on 2021-11-27 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20211127_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
