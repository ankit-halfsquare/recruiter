# Generated by Django 3.2 on 2022-11-09 04:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20221109_0443'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatetable',
            name='plateformOrReferral',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.platformorreferral'),
        ),
    ]
