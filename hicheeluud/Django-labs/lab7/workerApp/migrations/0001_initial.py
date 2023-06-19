# Generated by Django 4.1.5 on 2023-03-21 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dbApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wname', models.CharField(max_length=256)),
                ('bid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dbApp.branch')),
            ],
            options={
                'db_table': 'tbl_worker',
            },
        ),
    ]
