# Generated by Django 4.0 on 2022-03-09 07:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_ourworks_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=128, verbose_name="To'liq ismi")),
                ('phone', models.CharField(max_length=128, verbose_name='Telefon raqami')),
                ('short_description', models.TextField(verbose_name="Qisqacha ma'lumoti")),
                ('photo', models.ImageField(upload_to='partners/photo', verbose_name='Rasmi')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=128, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Nomi'),
        ),
        migrations.AlterField(
            model_name='ourworks',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='works', to='myapp.category', verbose_name='Kategoriyasi'),
        ),
        migrations.AlterField(
            model_name='ourworks',
            name='description',
            field=models.TextField(verbose_name="Ma'lumoti"),
        ),
    ]
