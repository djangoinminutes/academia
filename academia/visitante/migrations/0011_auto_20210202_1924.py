# Generated by Django 3.1.4 on 2021-02-02 19:24

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('visitante', '0010_auto_20210202_0321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle',
            name='texto',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
