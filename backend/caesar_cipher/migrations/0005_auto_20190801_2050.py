# Generated by Django 2.2.3 on 2019-08-01 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('caesar_cipher', '0004_auto_20190730_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cipher',
            name='content_decode',
            field=models.CharField(max_length=100, null=True),
        ),
    ]