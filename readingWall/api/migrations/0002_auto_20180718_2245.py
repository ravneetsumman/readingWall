# Generated by Django 2.0.7 on 2018-07-18 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connections',
            name='request_status',
            field=models.IntegerField(choices=[(1, 'pending'), (2, 'accepted'), (3, 'rejected'), (4, 'cancelled')], default=1),
        ),
    ]
