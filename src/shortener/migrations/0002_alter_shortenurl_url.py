# Generated by Django 3.2.15 on 2022-09-07 10:51

from django.db import migrations, models
import shortener.validators


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortenurl',
            name='url',
            field=models.TextField(validators=[shortener.validators.validate_url]),
        ),
    ]
