# Generated by Django 4.1.1 on 2022-10-19 19:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crime', '0002_rename_evidence_register_crime_evidence_of_crime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_crime',
            old_name='Evidence_of_crime',
            new_name='evidence_of_crime',
        ),
    ]
