# Generated by Django 3.1.4 on 2021-01-25 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210110_0121'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='completo',
            field=models.BooleanField(default=False),
        ),
    ]
