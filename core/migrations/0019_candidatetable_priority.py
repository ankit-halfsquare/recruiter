# Generated by Django 3.2 on 2022-11-02 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_remove_candidatetable_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatetable',
            name='priority',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='core.candidatepriority'),
        ),
    ]