# Generated by Django 4.0 on 2022-03-10 05:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_ourworks_address_ourworks_floor_ourworks_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='ourworks',
            name='pdf',
            field=models.FileField(default='', upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf'])], verbose_name='Fayl'),
            preserve_default=False,
        ),
    ]