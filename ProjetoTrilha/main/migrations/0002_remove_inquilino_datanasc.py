# Generated by Django 4.0.3 on 2022-03-28 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquilino',
            name='dataNasc',
        ),
    ]