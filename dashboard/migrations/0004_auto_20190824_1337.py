# Generated by Django 2.2.4 on 2019-08-24 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20190824_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='party',
            name='description',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='phone_number',
            field=models.CharField(blank=True, max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='party',
            name='rsvp_id',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]