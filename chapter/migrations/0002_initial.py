# Generated by Django 5.0.6 on 2024-05-16 11:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chapter', '0001_initial'),
        ('manga', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='manga',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manga.manga'),
        ),
    ]
