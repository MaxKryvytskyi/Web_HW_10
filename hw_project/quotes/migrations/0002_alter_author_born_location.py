# Generated by Django 4.2.10 on 2024-02-17 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='born_location',
            field=models.CharField(max_length=80),
        ),
    ]