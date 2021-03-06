# Generated by Django 2.1.5 on 2019-11-15 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0020_code_table_image_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='recommendation_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('serialNO', models.IntegerField(default=0)),
                ('link', models.CharField(max_length=300)),
                ('cardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.card_table')),
            ],
        ),
    ]
