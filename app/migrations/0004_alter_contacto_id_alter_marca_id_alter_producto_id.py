# Generated by Django 5.0.6 on 2024-06-11 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='marca',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
