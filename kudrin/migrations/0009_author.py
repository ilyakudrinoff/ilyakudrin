# Generated by Django 4.0.6 on 2022-09-17 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kudrin', '0008_buyquery_shirt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('text', models.TextField(verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новости',
                'ordering': ['-created_at', 'title'],
            },
        ),
    ]
