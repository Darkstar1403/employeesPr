# Generated by Django 3.1.4 on 2020-12-18 04:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_auto_20201217_2202'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='hoja_vida',
            field=ckeditor.fields.RichTextField(default='Texto'),
            preserve_default=False,
        ),
    ]
