# Generated by Django 4.2.1 on 2023-05-09 19:10

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0007_rename_branchid_producer_producer_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='producer',
            name='products',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]