# Generated by Django 5.1.1 on 2024-09-15 15:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ygo_collection', '0003_card_in_draft'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='in_bulk',
        ),
    ]
