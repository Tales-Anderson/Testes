# Generated by Django 4.0.3 on 2022-03-28 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inquilino',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField()),
                ('dataNasc', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Apartamento',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tamM3', models.IntegerField()),
                ('andar', models.IntegerField()),
                ('numero', models.IntegerField()),
                ('qtdQuartos', models.IntegerField()),
                ('qtdBanheiros', models.IntegerField()),
                ('descricao', models.CharField(max_length=255)),
                ('disponivel', models.BooleanField(default=True)),
                ('residente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.inquilino')),
            ],
        ),
    ]
