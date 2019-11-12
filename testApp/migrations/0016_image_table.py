# Generated by Django 2.1.5 on 2019-11-10 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0015_auto_20191109_1944'),
    ]

    operations = [
        migrations.CreateModel(
            name='image_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('serialNO', models.IntegerField(default=0)),
                ('upload', models.ImageField(upload_to='')),
                ('cardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.card_table')),
            ],
        ),
    ]