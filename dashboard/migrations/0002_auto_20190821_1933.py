# Generated by Django 2.2.4 on 2019-08-21 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='city',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='party',
            name='phone_number',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='party',
            name='state',
            field=models.CharField(blank=True, max_length=32),
        ),
        migrations.AlterField(
            model_name='party',
            name='street',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='party',
            name='zip_code',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
