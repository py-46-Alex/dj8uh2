# Generated by Django 4.1.4 on 2023-01-26 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0003_alter_advertisement_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
