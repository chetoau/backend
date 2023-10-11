# Generated by Django 4.2.6 on 2023-10-11 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('internpedia', '0003_review_internship_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='endDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='review',
            name='startDate',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
