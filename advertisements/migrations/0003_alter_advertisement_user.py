# Generated by Django 4.1.4 on 2023-01-26 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisements', '0002_user_remove_advertisement_creator_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertisement',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisements.user'),
        ),
    ]
