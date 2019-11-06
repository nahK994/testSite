# Generated by Django 2.1.5 on 2019-11-06 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_auto_20191106_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='textTable',
            fields=[
                ('textID', models.AutoField(primary_key=True, serialize=False)),
                ('paragraph', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='cardtable',
            options={'ordering': ['cardID']},
        ),
        migrations.AddField(
            model_name='texttable',
            name='cardID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.cardTable'),
        ),
    ]
