# Generated by Django 3.0.2 on 2020-02-03 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('img', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
