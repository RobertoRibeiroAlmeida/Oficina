# Generated by Django 4.2.6 on 2023-11-08 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=20)),
                ('nascimento', models.DateField()),
                ('celular1', models.CharField(blank=True, max_length=20, null=True)),
                ('celular2', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculos.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano_modelo', models.CharField(blank=True, max_length=4, null=True)),
                ('ano_fabricacao', models.CharField(blank=True, max_length=4, null=True)),
                ('placa', models.CharField(max_length=20)),
                ('cor', models.CharField(max_length=20)),
                ('chassis', models.CharField(blank=True, max_length=30, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculos.cliente')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculos.marca')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veiculos.modelo')),
            ],
        ),
    ]
