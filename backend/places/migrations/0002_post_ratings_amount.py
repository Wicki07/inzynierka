# Generated by Django 3.2.8 on 2022-04-21 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='ratings_amount',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
