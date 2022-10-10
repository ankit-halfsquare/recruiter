# Generated by Django 3.2 on 2022-10-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_company'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='status_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='company',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='files/'),
        ),
    ]
