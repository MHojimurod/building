# Generated by Django 4.0 on 2022-03-11 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_ourworks_pdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourworks',
            name='floor',
            field=models.PositiveIntegerField(verbose_name='Qavati'),
        ),
        migrations.AlterField(
            model_name='ourworks',
            name='size',
            field=models.PositiveIntegerField(verbose_name='Maydoni'),
        ),
    ]
