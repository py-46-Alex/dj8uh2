# Generated by Django 4.1.4 on 2023-01-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0004_alter_advertisement_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
    ]
