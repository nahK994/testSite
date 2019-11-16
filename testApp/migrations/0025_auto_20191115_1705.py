# Generated by Django 2.1.5 on 2019-11-15 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('testApp', '0024_auto_20191115_1531'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardsInfo',
            fields=[
                ('card_info_ID', models.AutoField(primary_key=True, serialize=False)),
                ('card_serial_NO', models.IntegerField(default=0)),
                ('card_title', models.CharField(max_length=35)),
                ('card_paragraph', models.CharField(max_length=200)),
                ('card_text', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('category_title', models.CharField(max_length=35, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Codes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code_title', models.CharField(max_length=35)),
                ('code_serial_NO', models.IntegerField(default=0)),
                ('code', models.TextField()),
                ('card_info_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.CardsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=35)),
                ('image_serial_NO', models.IntegerField(default=0)),
                ('image_height', models.IntegerField(default=0)),
                ('image_width', models.IntegerField(default=0)),
                ('image_upload', models.ImageField(upload_to='')),
                ('card_info_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.CardsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Recommendations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recommendation_title', models.CharField(max_length=30)),
                ('recommendation_serial_NO', models.IntegerField(default=0)),
                ('recommendation_link', models.CharField(max_length=300)),
                ('card_info_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.CardsInfo')),
            ],
        ),
        migrations.AddField(
            model_name='cardsinfo',
            name='category_title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testApp.Categories'),
        ),
    ]