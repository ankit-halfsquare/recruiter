# Generated by Django 3.2 on 2022-10-12 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('keyword_id', models.AutoField(primary_key=True, serialize=False)),
                ('text', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'keyword',
                'managed': False,
            },
        ),
    ]