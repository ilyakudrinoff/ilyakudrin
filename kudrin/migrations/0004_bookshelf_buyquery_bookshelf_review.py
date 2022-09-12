# Generated by Django 4.0.6 on 2022-09-12 05:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kudrin', '0003_buyquery_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookshelf',
            name='buyquery',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kudrin.buyquery', verbose_name='Заявка на покупку'),
        ),
        migrations.AddField(
            model_name='bookshelf',
            name='review',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='kudrin.review', verbose_name='Отзывы'),
        ),
    ]
