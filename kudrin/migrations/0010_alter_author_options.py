# Generated by Django 4.1.10 on 2023-12-15 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kudrin', '0009_author'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-created_at', 'title'], 'verbose_name': 'Авторские записки', 'verbose_name_plural': 'Авторские записки'},
        ),
    ]