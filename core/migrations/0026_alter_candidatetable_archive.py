# Generated by Django 3.2 on 2022-11-14 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0025_candidatetable_custometemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatetable',
            name='archive',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
