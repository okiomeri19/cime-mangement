# Generated by Django 4.1.1 on 2022-10-19 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_crime',
            old_name='evidence',
            new_name='Evidence_of_crime',
        ),
    ]