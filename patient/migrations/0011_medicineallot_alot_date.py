# Generated by Django 2.0 on 2019-07-16 11:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0010_auto_20190102_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicineallot',
            name='alot_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
