# Generated by Django 2.2.10 on 2022-12-07 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pytest_django_crud', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
