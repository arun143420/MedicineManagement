# Generated by Django 2.0 on 2019-07-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0012_medicine_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
