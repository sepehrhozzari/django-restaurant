# Generated by Django 4.0.3 on 2022-04-21 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_setting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitesetting',
            name='phone_number',
            field=models.CharField(max_length=11, verbose_name='شماره تلفن'),
        ),
    ]
