# Generated by Django 3.0.3 on 2020-02-11 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_shop', '0002_auto_20200211_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(default='ideal', max_length=300),
        ),
    ]