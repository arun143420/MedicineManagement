# Generated by Django 2.0 on 2019-01-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0009_auto_20190102_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='aadhar_id',
            field=models.CharField(default='------NA------', max_length=12),
        ),
    ]
