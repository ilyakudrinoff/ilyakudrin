# Generated by Django 4.0.6 on 2022-09-12 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kudrin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookshelf',
            name='buyquery',
        ),
        migrations.RemoveField(
            model_name='bookshelf',
            name='review',
        ),
        migrations.DeleteModel(
            name='BuyQuery',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]