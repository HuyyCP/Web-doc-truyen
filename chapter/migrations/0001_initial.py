# Generated by Django 5.0.6 on 2024-05-16 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('index', models.IntegerField()),
                ('idDrive', models.CharField(default='', max_length=100, unique=True)),
                ('uploadTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]