# Generated by Django 3.2.7 on 2021-10-23 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pre',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9),
        ),
    ]
