# Generated by Django 3.0.7 on 2023-07-07 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spare', '0009_jobcarditems_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobcardservice',
            name='service_price_final',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
