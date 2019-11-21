# Generated by Django 2.1.5 on 2019-11-21 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0025_auto_20191115_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='The_All_New_Images_From_GoogleDrive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=35)),
                ('Serial_NO', models.IntegerField(default=0)),
                ('Height', models.IntegerField(default=0)),
                ('Width', models.IntegerField(default=0)),
                ('Upload_Link', models.CharField(max_length=100)),
                ('card_info_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.CardsInfo')),
            ],
        ),
    ]