# Generated by Django 5.1.4 on 2025-03-06 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notesapp', '0003_remove_notemodel_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='notemodel',
            name='tags',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
