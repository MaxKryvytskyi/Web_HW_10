# Generated by Django 4.2.10 on 2024-03-20 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0003_alter_tag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='quotes.author'),
        ),
    ]