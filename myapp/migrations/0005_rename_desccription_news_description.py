# Generated by Django 4.0 on 2022-03-08 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_ourworks'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='desccription',
            new_name='description',
        ),
    ]