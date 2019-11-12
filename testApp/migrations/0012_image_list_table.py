# Generated by Django 2.1.5 on 2019-11-09 17:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0011_image_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_list_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('upload', django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to=''), blank=True, size=None)),
            ],
        ),
    ]