# Generated by Django 4.2.4 on 2023-08-08 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spare', '0014_remove_category_image_alter_category_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='damage',
            name='photo',
        ),
    ]