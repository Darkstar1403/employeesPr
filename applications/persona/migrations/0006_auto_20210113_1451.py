# Generated by Django 3.1.4 on 2021-01-13 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0005_empleado_fullname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
    ]
