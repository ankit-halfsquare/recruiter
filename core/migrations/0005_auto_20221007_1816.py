# Generated by Django 3.2 on 2022-10-07 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_candidatetable_candidatefilenameoriginal'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='status_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='position',
            old_name='status_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='status_name',
            new_name='name',
        ),
    ]
