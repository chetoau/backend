# Generated by Django 4.2.6 on 2023-10-11 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('internpedia', '0006_alter_review_enddate_alter_review_startdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='endDate',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='startDate',
            field=models.DateField(auto_now_add=True),
        ),
    ]
