# Generated by Django 4.0 on 2022-03-18 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_alter_banner_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Partner',
        ),
        migrations.RemoveField(
            model_name='ourworks',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
