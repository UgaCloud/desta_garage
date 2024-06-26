# Generated by Django 5.0.4 on 2024-04-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spare', '0015_remove_damage_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='UGX', max_length=10, unique=True)),
                ('desc', models.CharField(default='Ugandan Shillings', max_length=20)),
                ('cost', models.CharField(default='1', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('UG', 'Uganda'), ('KE', 'Kenya'), ('TZ', 'Tanzania'), ('RD', 'Rwanda'), ('BD', 'Burundi'), ('SD', 'South Sudan')], default='Uganda', max_length=40)),
                ('city', models.CharField(default='Kampala', max_length=40)),
                ('address', models.CharField(default='Kansanga Plot 10, Gaba Road', max_length=50)),
                ('postal', models.CharField(default='P. O. Box 104747 Kampala,Uganda', max_length=50)),
                ('website', models.CharField(default='www.uga-cloud.com', max_length=50)),
                ('company_official_name', models.CharField(default='UGACLOUD SERVICES (U) LTD', max_length=50)),
                ('mobile', models.CharField(blank=True, max_length=20, null=True)),
                ('office_phone_number1', models.CharField(blank=True, max_length=20, null=True)),
                ('office_phone_number2', models.CharField(blank=True, max_length=40, null=True)),
                ('logo', models.ImageField(upload_to='logo')),
                ('app_name', models.CharField(default='UGACloud Bakozi', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
