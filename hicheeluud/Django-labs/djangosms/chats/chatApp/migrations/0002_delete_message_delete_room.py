# Generated by Django 4.2 on 2023-04-23 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatApp', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
    ]