# Generated by Django 4.2.4 on 2024-04-29 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spare', '0016_currency_sitesetting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobcarditems',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items_mesurement', to='spare.itemmeasurement'),
        ),
    ]
